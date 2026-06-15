from imagekitio import ImageKit
from config import IMAGEKIT_PRIVATE_KEY, IMAGEKIT_URL_ENDPOINT

imagekit = ImageKit(private_key=IMAGEKIT_PRIVATE_KEY)

def upload_file(file_bytes: bytes, file_name: str, folder: str, content_type: str = "image/png") -> str:
    """Upload a file to ImageKit and return the CDN URL."""

    result = imagekit.files.upload(
        file=(file_bytes, file_name, content_type),
        file_name=file_name,
        folder=folder,
        private_file=False,
        use_unique_file_name=False,
    )
    return result.url

def 