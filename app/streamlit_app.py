from __future__ import annotations
import streamlit as st

from src.graph.state import create_initial_state
from src.graph.workflow import execute_workflow


def main() -> None:
    st.set_page_config(page_title="Multimodal AI App", layout="wide")
    st.title("Multimodal AI Web App")

    with st.sidebar:
        st.header("Input Configuration")
        target_modality = st.selectbox(
            "Select output modality",
            [
                "text",
                "image",
                "audio",
                "video",
                "audio_to_text",
                "image_to_text",
                "video_to_text",
            ],
        )

    st.markdown("## User Input")
    text_query = st.text_area("Text prompt", value="", height=150)
    input_path = st.text_input("Input file path (optional)")

    if st.button("Run Workflow"):
        state = create_initial_state(
            text_query=text_query,
            input_path=input_path,
            input_type="text" if text_query else "file",
            target_modality=target_modality,
        )
        state = execute_workflow(state)

        st.markdown("### Workflow Result")
        st.write(state)

        if state.get("output_text"):
            st.markdown("#### Output text")
            st.write(state["output_text"])

        if state.get("output_path"):
            st.markdown("#### Output path")
            st.write(state["output_path"])


if __name__ == "__main__":
    main()
