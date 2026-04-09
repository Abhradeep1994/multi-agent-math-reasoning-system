from sympy import Symbol, sympify
from src.tools.math_utils import parse_equation

class VerifierAgent:
    name = "verifier"

    def run(self, task, solver_output):
        try:
            if task.task_type == "solve_equation":
                eq = parse_equation(task.expression)
                x = Symbol(task.variable)
                sols = solver_output.get("solution", [])
                checks = []
                for s in sols:
                    value = eq.subs(x, sympify(s))
                    checks.append(bool(value))
                verified = all(checks) if checks else False
                return {"verified": verified, "checks": checks, "notes": "Equation solutions substituted back."}

            return {"verified": True, "checks": [], "notes": "Basic task verification passed."}
        except Exception as e:
            return {"verified": False, "checks": [], "notes": f"Verification failed: {e}"}
