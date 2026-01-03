from abc import ABC, abstractmethod
from app.schemas.prompt import PromptRequest

class BasePromptGenerator(ABC):

    @abstractmethod
    def generate(self, data: PromptRequest) -> str:
        pass
