from __future__ import annotations
from typing import Callable, Dict

from .state import GraphState
from .nodes import (
    text_to_text_node,
    text_to_image_node,
    image_to_text_node,
    text_to_audio_node,
    audio_to_text_node,
    text_to_video_node,
    video_to_text_node,
)

WORKFLOW_MAP: Dict[str, Callable[[GraphState], GraphState]] = {
    "text": text_to_text_node,
    "image": text_to_image_node,
    "image_to_text": image_to_text_node,
    "audio": text_to_audio_node,
    "audio_to_text": audio_to_text_node,
    "video": text_to_video_node,
    "video_to_text": video_to_text_node,
}


def route_by_target(state: GraphState) -> Callable[[GraphState], GraphState]:
    target_modality = state.get("target_modality", "text") or "text"
    target_modality = target_modality.lower()

    if target_modality in ("text", "text_to_text"):
        return text_to_text_node
    if target_modality == "image":
        return text_to_image_node
    if target_modality == "image_to_text":
        return image_to_text_node
    if target_modality == "audio":
        return text_to_audio_node
    if target_modality == "audio_to_text":
        return audio_to_text_node
    if target_modality == "video":
        return text_to_video_node
    if target_modality == "video_to_text":
        return video_to_text_node

    return text_to_text_node


def execute_workflow(state: GraphState) -> GraphState:
    node = route_by_target(state)
    return node(state)


def compile_state_graph() -> Dict[str, Callable[[GraphState], GraphState]]:
    """Return the workflow map for inspection or future LangGraph compilation."""
    return WORKFLOW_MAP
