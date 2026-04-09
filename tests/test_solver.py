from src.agents.interpreter import InterpreterAgent
from src.agents.solver import SolverAgent

def test_solver_equation():
    task = InterpreterAgent().run("x**2 - 5*x + 6 = 0")
    result = SolverAgent().run(task)
    assert "2" in result["solution"] and "3" in result["solution"]
