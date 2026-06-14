from __future__ import annotations
from typing import TypedDict, List, Optional, Dict, Any


class GraphState(TypedDict, total=False):
    input_path: str
    input_type: str
    output_type: str
    text_query: str
    target_modality: str
    intermediate_responses: List[str]
    output_path: str
    output_text: str
    error: Optional[str]
    metadata: Dict[str, Any]


def create_initial_state(
    *,
    text_query: str = "",
    input_path: str = "",
    input_type: str = "text",
    target_modality: str = "text",
) -> GraphState:
    return {
        "input_path": input_path,
        "input_type": input_type,
        "output_type": "",
        "text_query": text_query,
        "target_modality": target_modality,
        "intermediate_responses": [],
        "output_path": "",
        "output_text": "",
        "error": None,
        "metadata": {},
    }
