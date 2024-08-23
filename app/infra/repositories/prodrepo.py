from asyncio import Task
from dataclasses import dataclass, field

from domain.entities.product import User
from infra.repositories.baserepo import BaseRepository


@dataclass
class MemoryRepository(BaseRepository):
    _saved_tasks: list[Task] = field(
        default_factory=list,
        kw_only=True,
    )
    _saved_user: list[User] = field(
        default_factory=list,
        kw_only=True,
    )
    
    # async def check_chat_exists_by_title(self, oid_task: str) -> bool:
        
    #     try:
    #         return bool(next(
    #             task for task in self._saved_tasks if task.oid == oid_task
    #         ))
    #     except StopIteration:
    #         return False
    
    async def add_task(self, task:Task) -> None:
        self._saved_tasks.append(task)
    
    async def add_user(self, user:User) -> None:
        self._saved_user.append(user)