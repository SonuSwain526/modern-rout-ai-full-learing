from __future__ import annotations
import os
from pathlib import Path
from typing import Dict

from dotenv import load_dotenv

load_dotenv(dotenv_path=Path(__file__).resolve().parent.parent / ".env")

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY", "")
GROQ_API_KEY = os.getenv("GROQ_API_KEY", "")
HF_API_KEY = os.getenv("HUGGINGFACE_API_KEY", "")

DEFAULT_PROVIDER = os.getenv("DEFAULT_PROVIDER", "openai")

MODEL_MAP: Dict[str, Dict[str, str]] = {
    "openai": {
        "text_to_text": "gpt-4o-mini",
        "text_to_image": "gpt-image-1",
        "text_to_audio": "gpt-audio-1",
        "text_to_video": "gpt-video-1",
    },
    "google": {
        "text_to_text": "gemini-pro",
        "text_to_image": "image-bison",
        "text_to_audio": "audio-bison",
        "text_to_video": "video-bison",
    },
    "huggingface": {
        "text_to_text": "facebook/bart-large-cnn",
        "text_to_image": "stabilityai/stable-diffusion-2",
    },
}


def get_model(provider: str, modality: str) -> str:
    provider = provider.lower()
    return MODEL_MAP.get(provider, MODEL_MAP[DEFAULT_PROVIDER]).get(modality, "")
