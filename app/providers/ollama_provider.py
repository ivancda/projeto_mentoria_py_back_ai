import httpx
from app.providers.llm_provider import LLMProvider
from app.core.config import settings

class OllamaProvider(LLMProvider):

    def review(self, code: str) -> str:
        payload = {
            "model": settings.OLLAMA_MODEL,
            "prompt": code,
            "stream": False,
        }

        response = httpx.post(f"{settings.OLLAMA_URL}/api/generate", json=payload, timeout=120)
        response.raise_for_status()

        return response.json()["response"]