import asyncio
import logging

from sqlmodel import Session, select
from database import engine
from model import Thumbnail, Job
from services.gemini_service import generate_thumbnail
from services.imagekit_service import upload_file

logger = logging.getLogger(__name__)

STYLES = {
    "bold and dramatic": 
        ("Create a bold and dramatic thumbnail with high contrast," 
         "cinematic lighting, dark moody background and powerful composition. "
         "The person's face should be prominent with a dramatic expression."
    ),
    "clean and minimal": 
        ("Create a clean and minimal thumbnail with bright lighting," 
         "white/light background, modern professional aesthetics, plenty of."
         "whitespace, and sharp clean composition. The person should look" 
         "approachable and professional."
    ),
    "vibrant and energetic": 
        ("Create a vibrant and energetic thumbnail with colorful gradients", 
         "dynamic angles, eye-catching pop-art style colors, and energetic. "
         "Composition. The person should have an excited or engaging expression."
    )
}

STYLE_ORDER = ["bold_dramatic","clean_minimal","vibrant_energetic"]