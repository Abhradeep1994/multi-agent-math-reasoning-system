def interpreter_prompt(problem: str) -> str:
    return f"Classify the math task and extract the expression: {problem}"

def explainer_prompt(problem: str, solution: str, verified: bool) -> str:
    return (
        f"Explain this math solution in simple steps.\n"
        f"Problem: {problem}\nSolution: {solution}\nVerified: {verified}"
    )

def critic_prompt(problem: str, solution: str, verifier_notes: str) -> str:
    return (
        f"Review the following attempt for mathematical correctness and clarity.\n"
        f"Problem: {problem}\nSolution: {solution}\nVerifier: {verifier_notes}"
    )
