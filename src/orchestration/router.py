def route_task(task):
    return {
        "needs_verification": task.task_type in {"solve_equation", "differentiate", "integrate", "simplify"},
        "needs_visualization": task.task_type == "plot",
    }
