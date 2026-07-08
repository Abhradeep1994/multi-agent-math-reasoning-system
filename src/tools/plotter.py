from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt
from sympy import Symbol, lambdify, sympify

def plot_expression(expr: str, output_path: str, variable: str = "x", low: float = -10, high: float = 10, points: int = 400):
    x = Symbol(variable)
    sym_expr = sympify(expr)
    f = lambdify(x, sym_expr, "numpy")
    xs = np.linspace(low, high, points)
    with np.errstate(all="ignore"):
        ys = f(xs)
        ys = np.asarray(ys, dtype=float) * np.ones_like(xs)

    # Break the line at discontinuities/asymptotes instead of drawing a
    # vertical spike through them (e.g. plotting 1/x near x=0).
    finite = np.isfinite(ys)
    if finite.any():
        typical_scale = np.nanpercentile(np.abs(ys[finite]), 95) or 1.0
        extreme = np.abs(ys) > max(typical_scale * 20, 1e6)
        ys = np.where(finite & ~extreme, ys, np.nan)

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
