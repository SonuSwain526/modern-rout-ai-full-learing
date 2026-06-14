from __future__ import annotations
from typing import List

from .state import GraphState
from src.services.text_service import text_to_text, text_to_audio
from src.services.image_service import text_to_image, image_to_text
from src.services.audio_service import audio_to_text
from src.services.video_service import text_to_video, video_to_text


def _append_response(state: GraphState, value: str) -> None:
    history: List[str] = state.get("intermediate_responses", []) or []
    history.append(value)
    state["intermediate_responses"] = history


def text_to_text_node(state: GraphState) -> GraphState:
    prompt = state.get("text_query", "")
    _append_response(state, prompt)
    response = text_to_text(prompt)
    state["output_text"] = response
    state["output_type"] = "text"
    return state


def text_to_image_node(state: GraphState) -> GraphState:
    prompt = state.get("text_query", "")
    _append_response(state, prompt)
    output_path = text_to_image(prompt)
    state["output_path"] = output_path
    state["output_type"] = "image"
    return state


def image_to_text_node(state: GraphState) -> GraphState:
    image_path = state.get("input_path", "")
    description = image_to_text(image_path)
    _append_response(state, description)
    state["output_text"] = description
    state["output_type"] = "text"
    return state


def text_to_audio_node(state: GraphState) -> GraphState:
    prompt = state.get("text_query", "")
    _append_response(state, prompt)
    output_path = text_to_audio(prompt)
    state["output_path"] = output_path
    state["output_type"] = "audio"
    return state


def audio_to_text_node(state: GraphState) -> GraphState:
    audio_path = state.get("input_path", "")
    transcript = audio_to_text(audio_path)
    _append_response(state, transcript)
    state["output_text"] = transcript
    state["output_type"] = "text"
    return state


def text_to_video_node(state: GraphState) -> GraphState:
    prompt = state.get("text_query", "")
    _append_response(state, prompt)
    output_path = text_to_video(prompt)
    state["output_path"] = output_path
    state["output_type"] = "video"
    return state


def video_to_text_node(state: GraphState) -> GraphState:
    video_path = state.get("input_path", "")
    summary = video_to_text(video_path)
    _append_response(state, summary)
    state["output_text"] = summary
    state["output_type"] = "text"
    return state
