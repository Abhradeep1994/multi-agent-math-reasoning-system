import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[1]))

import streamlit as st
from src.orchestration.workflow import MathReasoningWorkflow

st.set_page_config(page_title="Multi-Agent Math Reasoning", layout="wide")
st.title("Multi-Agent Math Reasoning & Visualization System")

problem = st.text_input("Enter a math problem", "Solve x**2 - 5*x + 6 = 0")

if st.button("Run"):
    workflow = MathReasoningWorkflow()
    result = workflow.run(problem, outputs_dir="outputs")

    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Result")
        st.json(result)

    with col2:
        st.subheader("Explanation")
        st.write(result["explainer_output"]["explanation"])
        plot_path = result["visualizer_output"].get("plot_path")
        if plot_path:
            st.image(plot_path, caption="Generated plot")
