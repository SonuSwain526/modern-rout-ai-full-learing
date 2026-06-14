from __future__ import annotations
from pathlib import Path
from typing import Optional

from src.config import DEFAULT_PROVIDER, get_model


def audio_to_text(audio_path: str, provider: str = DEFAULT_PROVIDER) -> str:
    """Placeholder audio transcription."""
    model = get_model(provider, "audio_to_text")
    return f"[{provider} | {model}] transcription for audio at {audio_path}."
