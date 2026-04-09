class CriticAgent:
    name = "critic"

    def run(self, task, solver_output, verifier_output, explainer_output):
        score = 1.0 if verifier_output.get("verified") else 0.3
        feedback = "High confidence result." if score > 0.8 else "Low confidence; review manually."
        return {"confidence_score": score, "feedback": feedback}
