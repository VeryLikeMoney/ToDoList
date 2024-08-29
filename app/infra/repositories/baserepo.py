from abc import ABC, abstractmethod
from asyncio import Task
from dataclasses import dataclass, field

from domain.entities.product import User


@dataclass
class BaseTaskRepository(ABC):
    @abstractmethod
    async def check_task_exists_by_oid(self, oid_task: str) -> bool:
        ...
    
    @abstractmethod
    async def add_task(self, chat: Task) -> None:
        ...

@dataclass
class BaseUserRepository(ABC):
    @abstractmethod
    async def check_user_exists_by_oid(self,oid_user:str) -> bool:
        ...
    
    @abstractmethod
    async def get_user_one(self, oid_user: str) -> User:
        ...
    
    @abstractmethod
    async def add_user(self, user: User) -> User:
        ...