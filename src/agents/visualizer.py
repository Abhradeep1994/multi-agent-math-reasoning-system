from src.tools.plotter import plot_expression

class VisualizationAgent:
    name = "visualizer"

    def run(self, task, outputs_dir: str = "outputs"):
        if task.task_type == "plot":
            path = plot_expression(task.expression, f"{outputs_dir}/plot.png", variable=task.variable)
            return {"plot_path": path}
        return {"plot_path": None}
