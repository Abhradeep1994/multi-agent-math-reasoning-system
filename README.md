# Multi-Agent Math Reasoning System

A plug-and-run starter repository for a **self-correcting multi-agent AI system**
that can interpret, solve, verify, explain, and visualize mathematical problems.

## What this project does
- Parses a math problem into a structured task
- Uses a solver agent to attempt a solution
- Uses a verifier agent to check the result with SymPy
- Generates plots for functions when possible
- Produces a step-by-step explanation
- Scores agreement and confidence for basic evaluation

## Architecture
User Input -> Interpreter -> Solver -> Verifier -> Visualizer -> Explainer -> Critic

## Quick start

```bash
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env
python src/main.py --problem "Solve x**2 - 5*x + 6 = 0"
streamlit run app/streamlit_app.py
```

## Example prompts
- `Solve x**2 - 5*x + 6 = 0`
- `Differentiate sin(x) * x**2`
- `Plot sin(x) + x**2`
- `Integrate x**2 * exp(x)`

This starter runs out of the box with SymPy + matplotlib + Streamlit.

## Input examples

Use inputs like these in the CLI or Streamlit app:

- `Solve x**2 - 5*x + 6 = 0`
- `plot sin(x) + x**2`
- `differentiate x**3 + 2*x`
- `integrate x**2`
