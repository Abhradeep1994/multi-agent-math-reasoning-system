from src.agents.interpreter import InterpreterAgent
from src.agents.solver import SolverAgent
from src.agents.verifier import VerifierAgent
from src.agents.visualizer import VisualizationAgent
from src.agents.explainer import ExplainerAgent
from src.agents.critic import CriticAgent
from src.orchestration.router import route_task

class MathReasoningWorkflow:
    def __init__(self):
        self.interpreter = InterpreterAgent()
        self.solver = SolverAgent()
        self.verifier = VerifierAgent()
        self.visualizer = VisualizationAgent()
        self.explainer = ExplainerAgent()
        self.critic = CriticAgent()

    def run(self, problem: str, outputs_dir: str = "outputs"):
        task = self.interpreter.run(problem)
        route = route_task(task)

        try:
            solver_output = self.solver.run(task)
        except Exception as e:
            error_note = (
                f"Could not solve/parse this expression ({e.__class__.__name__}: {e}). "
                "Check the syntax — use ** for powers and * for multiplication, "
                "e.g. 'x**2 - 5*x + 6 = 0'."
            )
            return {
                "task": task.model_dump(),
                "solver_output": {"solution": None, "method": "error", "error": str(e)},
                "verifier_output": {"verified": False, "checks": [], "notes": error_note},
                "visualizer_output": {"plot_path": None},
                "explainer_output": {"explanation": error_note},
                "critic_output": {"confidence_score": 0.0, "feedback": "Could not process input; please revise and retry."},
            }

        verifier_output = self.verifier.run(task, solver_output) if route["needs_verification"] else {"verified": True, "notes": "Skipped"}

        try:
            visualizer_output = self.visualizer.run(task, outputs_dir=outputs_dir) if route["needs_visualization"] else {"plot_path": None}
        except Exception as e:
            visualizer_output = {"plot_path": None, "error": f"Plot generation failed: {e}"}

        explainer_output = self.explainer.run(task, solver_output, verifier_output)
        critic_output = self.critic.run(task, solver_output, verifier_output, explainer_output)

        return {
            "task": task.model_dump(),
            "solver_output": solver_output,
            "verifier_output": verifier_output,
            "visualizer_output": visualizer_output,
            "explainer_output": explainer_output,
            "critic_output": critic_output,
        }
