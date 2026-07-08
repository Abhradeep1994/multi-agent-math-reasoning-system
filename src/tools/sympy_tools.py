from sympy import Symbol, diff, integrate, solveset, S, simplify, solve
from src.tools.math_utils import parse_equation, safe_sympify

def solve_equation(problem: str, variable: str = "x"):
    """Returns (solutions, exhaustive).

    solveset() can return an infinite set (e.g. Union of ImageSets for
    periodic equations like sin(x) = 0). Calling list() on that hangs
    forever, so we only enumerate when the set is confirmed finite.
    Note: `isinstance(sol_set, FiniteSet)` is NOT sufficient here — the
    "no solutions" case (EmptySet, e.g. for a contradiction like 0 = 1)
    is finite but is its own sympy class, not a FiniteSet instance. We use
    `sol_set.is_finite_set` instead, which correctly returns True for both
    FiniteSet and EmptySet, and None for sets like the periodic union above.
    For genuinely infinite/indeterminate sets we fall back to sympy.solve()
    for a finite, representative sample and flag the result as non-exhaustive.
    """
    symbol = Symbol(variable)
    eq = parse_equation(problem)
    sol_set = solveset(eq, symbol, domain=S.Complexes)

    if sol_set.is_finite_set:
        return list(sol_set), True

    representative = solve(eq, symbol)
    return representative, False

def differentiate_expression(expr: str, variable: str = "x"):
    symbol = Symbol(variable)
    return simplify(diff(safe_sympify(expr), symbol))

def integrate_expression(expr: str, variable: str = "x"):
    symbol = Symbol(variable)
    return simplify(integrate(safe_sympify(expr), symbol))

def simplify_expression(expr: str):
    return simplify(safe_sympify(expr))
