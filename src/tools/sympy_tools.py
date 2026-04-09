from sympy import Symbol, diff, integrate, solveset, S, simplify
from src.tools.math_utils import parse_equation, safe_sympify

def solve_equation(problem: str, variable: str = "x"):
    symbol = Symbol(variable)
    eq = parse_equation(problem)
    return list(solveset(eq, symbol, domain=S.Complexes))

def differentiate_expression(expr: str, variable: str = "x"):
    symbol = Symbol(variable)
    return simplify(diff(safe_sympify(expr), symbol))

def integrate_expression(expr: str, variable: str = "x"):
    symbol = Symbol(variable)
    return simplify(integrate(safe_sympify(expr), symbol))

def simplify_expression(expr: str):
    return simplify(safe_sympify(expr))
