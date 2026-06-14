from __future__ import annotations
from flask import Flask, render_template, request

from src.graph.state import create_initial_state
from src.graph.workflow import execute_workflow

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    state = None
    result = None

    if request.method == "POST":
        target_modality = request.form.get("target_modality", "text")
        text_query = request.form.get("text_query", "")
        input_path = request.form.get("input_path", "")

        state = create_initial_state(
            text_query=text_query,
            input_path=input_path,
            input_type="text" if text_query else "file",
            target_modality=target_modality,
        )
        result = execute_workflow(state)

    return render_template(
        "index.html",
        state=state,
        result=result,
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8501, debug=True)
