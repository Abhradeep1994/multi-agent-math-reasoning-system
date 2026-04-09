class ExplainerAgent:
    name = "explainer"

    def run(self, task, solver_output, verifier_output):
        verified = verifier_output.get("verified", False)
        solution = solver_output.get("solution")
        explanation = (
            f"Task type: {task.task_type}. "
            f"The system computed the result as {solution}. "
            f"Verification status: {'passed' if verified else 'failed'}."
        )
        return {"explanation": explanation}
