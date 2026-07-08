import numpy as np
from sympy import Symbol, sympify, diff, simplify, lambdify

from src.tools.math_utils import parse_equation, safe_sympify

SAMPLE_POINTS = [-2.0, -0.5, 0.7, 1.3, 3.0]


class VerifierAgent:
    name = "verifier"

    def run(self, task, solver_output):
        try:
            if task.task_type == "solve_equation":
                return self._verify_equation(task, solver_output)
            if task.task_type == "differentiate":
                return self._verify_derivative(task, solver_output)
            if task.task_type == "integrate":
                return self._verify_integral(task, solver_output)
            if task.task_type == "simplify":
                return self._verify_equivalence(task, solver_output)
            return {"verified": True, "checks": [], "notes": "No verification implemented for this task type."}
        except Exception as e:
            return {"verified": False, "checks": [], "notes": f"Verification failed: {e}"}

    def _verify_equation(self, task, solver_output):
        eq = parse_equation(task.expression)
        x = Symbol(task.variable)
        sols = solver_output.get("solution") or []
        checks = []
        for s in sols:
            value = eq.subs(x, sympify(s))
            checks.append(bool(value))
        verified = all(checks) if checks else False
        notes = "Equation solutions substituted back."
        if not solver_output.get("exhaustive", True):
            notes += " Note: this equation has an infinite solution family; only a representative solution was checked."
        return {"verified": verified, "checks": checks, "notes": notes}

    def _verify_derivative(self, task, solver_output):
        # Independent check: compare the claimed derivative against a
        # central-difference numerical estimate of the original function,
        # rather than just re-running sympy.diff() a second time.
        x = Symbol(task.variable)
        original = safe_sympify(task.expression)
        claimed = sympify(solver_output.get("solution"))
        f = lambdify(x, original, "numpy")
        g = lambdify(x, claimed, "numpy")

        checks = []
        h = 1e-5
        for point in SAMPLE_POINTS:
            try:
                numeric_derivative = (float(f(point + h)) - float(f(point - h))) / (2 * h)
                claimed_value = float(g(point))
                checks.append(bool(np.isclose(numeric_derivative, claimed_value, atol=1e-3, rtol=1e-3)))
            except Exception:
                continue

        verified = bool(checks) and all(checks)
        notes = "Checked via central-difference numerical approximation at sample points."
        if not checks:
            notes = "Could not evaluate the derivative numerically at any sample point."
        return {"verified": verified, "checks": checks, "notes": notes}

    def _verify_integral(self, task, solver_output):
        # Fundamental theorem of calculus: differentiating the claimed
        # antiderivative should reproduce the original integrand.
        x = Symbol(task.variable)
        original = safe_sympify(task.expression)
        claimed = sympify(solver_output.get("solution"))
        difference = simplify(diff(claimed, x) - original)
        verified = difference == 0
        notes = "Checked by differentiating the antiderivative and comparing to the original integrand."
        if not verified:
            notes += f" Residual after differentiating back: {difference}"
        return {"verified": verified, "checks": [verified], "notes": notes}

    def _verify_equivalence(self, task, solver_output):
        # Used for the generic "simplify" fallback task: confirm the
        # simplified expression is numerically equivalent to the original.
        x = Symbol(task.variable)
        original = safe_sympify(task.expression)
        claimed = sympify(solver_output.get("solution"))
        f = lambdify(x, original, "numpy")
        g = lambdify(x, claimed, "numpy")

        checks = []
        for point in SAMPLE_POINTS:
            try:
                checks.append(bool(np.isclose(float(f(point)), float(g(point)), atol=1e-6, rtol=1e-6)))
            except Exception:
                continue

        verified = bool(checks) and all(checks)
        notes = "Checked numeric equivalence between original and simplified expressions at sample points."
        if not checks:
            notes = "Could not numerically evaluate the expressions at any sample point."
        return {"verified": verified, "checks": checks, "notes": notes}
