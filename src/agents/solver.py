from src.tools.sympy_tools import (
    solve_equation,
    differentiate_expression,
    integrate_expression,
    simplify_expression,
)

class SolverAgent:
    name = "solver"

    def run(self, task):
        if task.task_type == "solve_equation":
            solutions = solve_equation(task.expression, task.variable)
            return {"solution": [str(s) for s in solutions], "method": "sympy_solveset"}

        if task.task_type == "differentiate":
            result = differentiate_expression(task.expression, task.variable)
            return {"solution": str(result), "method": "sympy_diff"}

        if task.task_type == "integrate":
            result = integrate_expression(task.expression, task.variable)
            return {"solution": str(result), "method": "sympy_integrate"}

        if task.task_type in {"plot", "simplify"}:
            result = simplify_expression(task.expression)
            return {"solution": str(result), "method": "sympy_simplify"}

        return {"solution": "Unsupported task", "method": "unknown"}
