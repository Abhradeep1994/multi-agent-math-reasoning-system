from src.orchestration.workflow import MathReasoningWorkflow

def test_pipeline_runs():
    result = MathReasoningWorkflow().run("x**2 - 5*x + 6 = 0")
    assert "solver_output" in result
    assert result["verifier_output"]["verified"] is True
