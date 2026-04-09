def agreement_score(verifier_output: dict) -> float:
    return 1.0 if verifier_output.get("verified") else 0.0
