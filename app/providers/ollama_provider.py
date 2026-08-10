import logging
import time
import httpx
from tenacity import (
    retry,
    stop_after_attempt,
    wait_exponential,
    retry_if_exception_type,
    before_sleep_log,
)
from app.providers.llm_provider import LLMProvider
from app.providers.prompts import build_review_prompt
from app.core.config import settings

logger = logging.getLogger(__name__)


class OllamaProvider(LLMProvider):

    @retry(
        retry=retry_if_exception_type((httpx.ConnectError, httpx.TimeoutException)),
        stop=stop_after_attempt(3),
        wait=wait_exponential(multiplier=1, min=2, max=10),
        before_sleep=before_sleep_log(logger, logging.WARNING),
        reraise=True,
    )
    def review(self, code: str) -> str:
        payload = {
            "model": settings.OLLAMA_MODEL,
            "prompt": build_review_prompt(code),
            "stream": False,
        }

        logger.info("Sending request to Ollama (model=%s)", settings.OLLAMA_MODEL)
        start = time.monotonic()

        response = httpx.post(f"{settings.OLLAMA_URL}/api/generate", json=payload, timeout=60)
        response.raise_for_status()

        elapsed = time.monotonic() - start
        logger.info("Ollama responded in %.2fs", elapsed)

        return response.json()["response"]