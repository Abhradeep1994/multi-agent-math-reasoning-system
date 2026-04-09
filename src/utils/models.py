from pydantic import BaseModel, Field
from typing import Optional, Any

class MathTask(BaseModel):
    raw_problem: str
    task_type: str = Field(default="unknown")
    expression: Optional[str] = None
    variable: str = "x"

class AgentOutput(BaseModel):
    agent_name: str
    content: dict[str, Any]
