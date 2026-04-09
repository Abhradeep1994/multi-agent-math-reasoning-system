from src.evaluation.metrics import agreement_score

def evaluate_run(run_output: dict) -> dict:
    score = agreement_score(run_output.get("verifier_output", {}))
    return {
        "agreement_score": score,
        "confidence_score": run_output.get("critic_output", {}).get("confidence_score", 0.0),
    }
