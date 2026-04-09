from src.utils.logger import get_logger

logger = get_logger(__name__)

class MockLLMClient:
    def generate(self, prompt: str) -> str:
        logger.info("MockLLMClient invoked.")
        return f"[MOCK LLM RESPONSE]\n{prompt[:800]}"

def get_llm_client(provider: str = "mock"):
    return MockLLMClient()
