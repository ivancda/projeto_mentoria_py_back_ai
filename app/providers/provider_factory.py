from app.providers.llm_provider import LLMProvider
from app.providers.ollama_provider import OllamaProvider
from app.core.config import settings

def get_provider() -> LLMProvider:
    if settings.LLM_PROVIDER == "ollama":
        return OllamaProvider()

    raise ValueError(f"Provider desconhecido: '{settings.LLM_PROVIDER}'")