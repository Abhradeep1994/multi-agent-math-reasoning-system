from src.agents.interpreter import InterpreterAgent
from src.agents.solver import SolverAgent
from src.agents.verifier import VerifierAgent


def test_verifier_equation():
    task = InterpreterAgent().run("x**2 - 5*x + 6 = 0")
    solver_output = SolverAgent().run(task)
    verifier_output = VerifierAgent().run(task, solver_output)
    assert verifier_output["verified"] is True


def test_verifier_no_solution_is_not_mislabeled_infinite():
    # 0 = 1 has zero solutions (EmptySet), which is finite but NOT a
    # FiniteSet instance in sympy. Regression test for a bug where this
    # was incorrectly flagged as an "infinite solution family".
    task = InterpreterAgent().run("Solve 0 = 1")
    solver_output = SolverAgent().run(task)
    assert solver_output["exhaustive"] is True
    verifier_output = VerifierAgent().run(task, solver_output)
    assert verifier_output["verified"] is False
    assert "infinite" not in verifier_output["notes"].lower()


def test_verifier_catches_wrong_derivative():
    task = InterpreterAgent().run("Differentiate x**2")
    wrong_output = {"solution": "3*x"}  # correct is 2*x
    verifier_output = VerifierAgent().run(task, wrong_output)
    assert verifier_output["verified"] is False


def test_verifier_confirms_correct_derivative():
    task = InterpreterAgent().run("Differentiate x**2")
    correct_output = {"solution": "2*x"}
    verifier_output = VerifierAgent().run(task, correct_output)
    assert verifier_output["verified"] is True


def test_verifier_catches_wrong_integral():
    task = InterpreterAgent().run("Integrate x**2")
    wrong_output = {"solution": "x**4"}  # correct is x**3/3
    verifier_output = VerifierAgent().run(task, wrong_output)
    assert verifier_output["verified"] is False


def test_solve_equation_with_infinite_solutions_does_not_hang():
    # Regression test: sin(x) = 0 has infinitely many solutions. This must
    # return quickly with a representative (non-exhaustive) answer instead
    # of hanging forever trying to enumerate an infinite set.
    task = InterpreterAgent().run("Solve sin(x) = 0")
    solver_output = SolverAgent().run(task)
    assert solver_output["exhaustive"] is False
    assert len(solver_output["solution"]) > 0
