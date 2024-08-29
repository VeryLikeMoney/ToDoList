from asyncio import Task
from dataclasses import dataclass, field
from typing import Any, Coroutine

from domain.entities.product import User
from infra.repositories.baserepo import BaseTaskRepository, BaseUserRepository


@dataclass
class MemoryTaskRepository(BaseTaskRepository):
    _saved_tasks: list[Task] = field(
        default_factory=list,
        kw_only=True,
    )
    
    async def check_task_exists_by_oid(self, oid_task: str) -> bool:
        
        try:
            return bool(next(
                task for task in self._saved_tasks if task.oid == oid_task
            ))
        except StopIteration:
            return False
    
    async def add_task(self, task:Task) -> None:
        self._saved_tasks.append(task)


@dataclass
class MemoryUserReposiroty(BaseUserRepository):
    
    _saved_user: list[User] = field(
        default_factory=list,
        kw_only=True,
    )
    
    async def get_user_one(self, oid_user: str) -> User | None:
        user, *_ = [user for user in self._saved_user if user.oid==oid_user ]
        
        return user
    
    async def check_user_exists_by_oid(self, oid_user: str) -> bool:
        try:
            return bool(next(
                user for user in self._saved_user if user.oid == oid_user
            ))
        except StopIteration:
            return False
    
    async def add_user(self, user: User):
        self._saved_user.append(user)
    
    
