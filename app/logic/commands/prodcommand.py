
from dataclasses import dataclass
from typing import Any, Coroutine
from domain.entities.product import Task, User
from domain.values.product import Text, Title
from infra.repositories.baserepo import BaseTaskRepository, BaseUserRepository
from logic.commands.base import BaseCommand, BaseCommandHandler
from infra.exseptions.prod import User_with_mail_already_exists

@dataclass(frozen=True)
class CreateTaskCommand(BaseCommand):
    title: str
    creator_task: User 
    text_task: str
    

@dataclass(frozen=True)
class CreateTaskCommandHandler(BaseCommandHandler):
    repository: BaseTaskRepository
    
    async def handle(self, command: CreateTaskCommand) -> Task:
       
        #TODO чек task на валидность
        
        title = Title(command.title)
        text_task = Text(command.text_task)
        
        new_task = Task.create(creator_task=command.creator_task,
                        text_task=text_task,
                        title=title)
        await self.repository.add_task(new_task)
        
        return new_task


@dataclass(frozen=True)
class GetUserCommand(BaseCommand):
    user_oid: str

@dataclass(frozen=True)
class CreateUserCommand(BaseCommand):
    surname: str
    name: str
    patronymic: str
    mail: str
    department: str = ''
    phone: str = ''

@dataclass(frozen=True)
class CreateUserCommandHandler(BaseCommandHandler):
    repository: BaseUserRepository
    
    async def handle(self, command: CreateUserCommand) -> User:
        if await self.repository.check_task_exists_by_mail(command.mail):
            raise User_with_mail_already_exists(command.mail)
            
        new_user = User.create(
            command.surname,
            command.name,
            command.patronymic,
            command.mail,
            command.department,
            command.phone
        )
        await self.repository.add_user(new_user)
        
        return new_user

@dataclass(frozen=True)
class GetUserCommandHandler(BaseCommandHandler):
    repository: BaseUserRepository
    
    async def handle(self, command: GetUserCommand) -> User:
        #TODO чек task на валидность      
        
        user = await self.repository.get_user_one(command.user_oid)
        return user