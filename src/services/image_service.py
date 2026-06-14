from __future__ import annotations
from pathlib import Path
from typing import Optional

from src.config import DEFAULT_PROVIDER, get_model


def text_to_image(prompt: str, provider: str = DEFAULT_PROVIDER) -> str:
    """Placeholder text-to-image generation."""
    model = get_model(provider, "text_to_image")
    output_path = Path("media_vault") / "generated_image.png"
    output_path.parent.mkdir(parents=True, exist_ok=True)
    return str(output_path)


def image_to_text(image_path: str, provider: str = DEFAULT_PROVIDER) -> str:
    """Placeholder image captioning / OCR."""
    model = get_model(provider, "image_to_text")
    return f"[{provider} | {model}] caption for image at {image_path}."
