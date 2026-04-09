from src.agents.interpreter import InterpreterAgent

def test_interpreter_detects_plot():
    task = InterpreterAgent().run("Plot sin(x) + x**2")
    assert task.task_type == "plot"
