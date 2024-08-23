from abc import ABC, abstractmethod
from asyncio import Task
from dataclasses import dataclass, field


@dataclass
class BaseRepository(ABC):
    @abstractmethod
    async def check_chat_exists_by_title(self, title: str) -> bool:
        ...
    
    @abstractmethod
    async def add_task(self, chat: Task) -> None:
        ...