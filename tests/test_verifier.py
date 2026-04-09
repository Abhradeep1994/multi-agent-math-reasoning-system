from src.agents.interpreter import InterpreterAgent
from src.agents.solver import SolverAgent
from src.agents.verifier import VerifierAgent

def test_verifier_equation():
    task = InterpreterAgent().run("x**2 - 5*x + 6 = 0")
    solver_output = SolverAgent().run(task)
    verifier_output = VerifierAgent().run(task, solver_output)
    assert verifier_output["verified"] is True
