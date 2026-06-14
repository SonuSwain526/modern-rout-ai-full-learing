from __future__ import annotations
from pathlib import Path

from src.config import DEFAULT_PROVIDER, get_model


def text_to_video(prompt: str, provider: str = DEFAULT_PROVIDER) -> str:
    """Placeholder text-to-video generation."""
    model = get_model(provider, "text_to_video")
    output_path = Path("media_vault") / "generated_video.mp4"
    output_path.parent.mkdir(parents=True, exist_ok=True)
    return str(output_path)


def video_to_text(video_path: str, provider: str = DEFAULT_PROVIDER) -> str:
    """Placeholder video summarization / description."""
    model = get_model(provider, "video_to_text")
    return f"[{provider} | {model}] summary for video at {video_path}."
