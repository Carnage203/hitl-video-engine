from PIL import Image
from google import genai
from google.genai import types

from config import GOOGLE_GENAI_API_KEY

client = genai.AsyncClient(api_key=GOOGLE_GENAI_API_KEY)

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

    response = 


