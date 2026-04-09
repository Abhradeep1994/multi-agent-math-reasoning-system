from __future__ import annotations

import re
from sympy import Eq, sympify


LEADING_COMMAND_RE = re.compile(
    r"^\s*(solve|plot|visualize|graph|differentiate|derivative of|integrate|integral of)\s+",
    re.IGNORECASE,
)


def normalize_problem_text(problem: str) -> str:
    problem = problem.strip()
    problem = re.sub(r"\s+", " ", problem)
    return problem


def strip_leading_command(problem: str) -> str:
    return LEADING_COMMAND_RE.sub("", normalize_problem_text(problem)).strip()


def looks_like_plot_request(problem: str) -> bool:
    lowered = normalize_problem_text(problem).lower()
    return lowered.startswith(("plot ", "visualize ", "graph ")) or " plot " in f" {lowered} " or "visualize" in lowered


def looks_like_derivative_request(problem: str) -> bool:
    lowered = normalize_problem_text(problem).lower()
    return lowered.startswith(("differentiate ", "derivative of ")) or "derivative" in lowered


def looks_like_integral_request(problem: str) -> bool:
    lowered = normalize_problem_text(problem).lower()
    return lowered.startswith(("integrate ", "integral of ")) or "integral" in lowered


def looks_like_equation(problem: str) -> bool:
    return "=" in normalize_problem_text(problem)


def safe_sympify(expr: str):
    expr = strip_leading_command(expr)
    return sympify(expr)


def parse_equation(problem: str):
    cleaned = strip_leading_command(problem)
    left, right = cleaned.split("=", 1)
    return Eq(sympify(left.strip()), sympify(right.strip()))
