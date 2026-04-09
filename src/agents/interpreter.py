from src.utils.models import MathTask
from src.tools.math_utils import (
    looks_like_plot_request,
    looks_like_derivative_request,
    looks_like_integral_request,
    looks_like_equation,
    strip_leading_command,
    normalize_problem_text,
)

class InterpreterAgent:
    name = "interpreter"

    def run(self, problem: str) -> MathTask:
        raw = normalize_problem_text(problem)

        if looks_like_plot_request(raw):
            expr = strip_leading_command(raw)
            return MathTask(raw_problem=raw, task_type="plot", expression=expr)

        if looks_like_derivative_request(raw):
            expr = strip_leading_command(raw)
            return MathTask(raw_problem=raw, task_type="differentiate", expression=expr)

        if looks_like_integral_request(raw):
            expr = strip_leading_command(raw)
            return MathTask(raw_problem=raw, task_type="integrate", expression=expr)

        if looks_like_equation(raw):
            expr = strip_leading_command(raw)
            return MathTask(raw_problem=raw, task_type="solve_equation", expression=expr)

        return MathTask(raw_problem=raw, task_type="simplify", expression=strip_leading_command(raw))
