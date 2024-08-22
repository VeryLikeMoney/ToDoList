from dataclasses import dataclass, field
from datetime import datetime


from domain.entities.base import BaseEntity
from domain.values.product import Status, Title, Text

@dataclass
class User(BaseEntity):
    
    surname: str
    name: str
    patronymic: str
    mail: str
    department: str | None = None
    phone: str | None = None

    def __post_init__(self):
        # TODO: добавить добавление евента
        pass

@dataclass
class Task(BaseEntity):
    
    creator_task: User
    text_task: Text
    title: Title
    status: Status = field(
        default_factory=lambda: Status(Status.is_created())
    )
    created_at: datetime = field(
        default_factory=datetime.now,
        kw_only=True,
    )
    
    @classmethod
    def create_task(cls, creator_task: User, text_task: Text, title: Title) -> 'Task': 
        
        task = cls(creator_task, text_task, title)
        # TODO: добавить добавление евента
        
        return task
        