from abc import ABC, abstractmethod


class LLMProvider(ABC):

    # garante que qualquer subclasse obrigatoriamente implemente o método review
    @abstractmethod
    def review(self, code: str) -> str:
        pass