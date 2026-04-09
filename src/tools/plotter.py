from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt
from sympy import Symbol, lambdify, sympify

def plot_expression(expr: str, output_path: str, variable: str = "x", low: float = -10, high: float = 10, points: int = 400):
    x = Symbol(variable)
    sym_expr = sympify(expr)
    f = lambdify(x, sym_expr, "numpy")
    xs = np.linspace(low, high, points)
    ys = f(xs)

    out = Path(output_path)
    out.parent.mkdir(parents=True, exist_ok=True)

    plt.figure(figsize=(8, 5))
    plt.plot(xs, ys)
    plt.axhline(0)
    plt.axvline(0)
    plt.title(f"Plot of {expr}")
    plt.xlabel(variable)
    plt.ylabel("y")
    plt.tight_layout()
    plt.savefig(out)
    plt.close()
    return str(out)
