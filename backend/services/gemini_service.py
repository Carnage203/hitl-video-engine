from PIL import Image
from google import genai
from google.genai import types

from config import GOOGLE_GENAI_API_KEY

client = genai.Client(api_key=GOOGLE_GENAI_API_KEY)

aspect_ratio = "16:9"
resolution  = "2K"

async def generate_thumbnail(prompt: str, style_prompt: str, headshot_url: str) -> bytes:
    """Use the Responses API with gemini nano banana as a built-in image_generation tool.
    Pass the headshot URL directly as input_image 
    Returns raw PNG bytes.
    """

    full_prompt = (
        f"{style_prompt}\n\n"
        f"User request: {prompt}\n\n"
        "IMPORTANT: The generated thumbnail MUST prominently feature the person."
        "shown in the provided reference headshot image. Keep their likeness accurate."
    )

    response = await client.aio.models.generate_content(
            model = "gemini-3.1-flash-image",
            contents=[
            {
                "role": "user",
                "parts": [
                    {"file_data": {"file_uri": headshot_url, "mime_type": "image/jpeg"}},
                    {"text": full_prompt}
                ]
            }
        ],
        config=types.GenerateContentConfig(
            response_modalities=['IMAGE'],
             image_config={
                 "image": {"aspect_ratio": aspect_ratio, "image_size": resolution}
            },
        )
    )

    for part in response.parts:
        if image := part.as_image():
            return image
    
    raise RuntimeError("No image generation result found in the response")
