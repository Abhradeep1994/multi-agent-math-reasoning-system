from src.orchestration.workflow import MathReasoningWorkflow

def test_pipeline_runs():
    result = MathReasoningWorkflow().run("x**2 - 5*x + 6 = 0")
    assert "solver_output" in result
    assert result["verifier_output"]["verified"] is True


def test_pipeline_handles_unparseable_input_gracefully():
    # Regression test: this used to crash with an uncaught SympifyError
    # and a raw traceback instead of returning a usable result.
    result = MathReasoningWorkflow().run("asdkfj qqqq")
    assert "solver_output" in result
    assert result["critic_output"]["confidence_score"] == 0.0
    assert "explanation" in result["explainer_output"]
