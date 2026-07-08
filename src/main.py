import argparse
import json
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.append(str(PROJECT_ROOT))

from src.orchestration.workflow import MathReasoningWorkflow
from src.evaluation.evaluator import evaluate_run
from src.utils.helpers import ensure_dir


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--problem", type=str, required=True, help="Math problem to solve")
    parser.add_argument("--outputs-dir", type=str, default="outputs")
    args = parser.parse_args()

    try:
        ensure_dir(args.outputs_dir)
        workflow = MathReasoningWorkflow()
        result = workflow.run(args.problem, outputs_dir=args.outputs_dir)
        result["evaluation"] = evaluate_run(result)

        out_path = Path(args.outputs_dir) / "result.json"
        out_path.write_text(json.dumps(result, indent=2), encoding="utf-8")
        print(json.dumps(result, indent=2))
        print(f"Saved result to {out_path}")
    except Exception as e:
        print(f"Error: could not process this problem ({e.__class__.__name__}: {e}).", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
