from src.orchestration.workflow import MathReasoningWorkflow
from src.evaluation.benchmarks import BENCHMARK_PROBLEMS
from src.evaluation.evaluator import evaluate_run

workflow = MathReasoningWorkflow()
for problem in BENCHMARK_PROBLEMS:
    result = workflow.run(problem)
    metrics = evaluate_run(result)
    print(problem)
    print(metrics)
    print("-" * 40)
