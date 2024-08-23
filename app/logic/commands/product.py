
from dataclasses import dataclass
from domain.entities.product import Task, User
from domain.values.product import Text, Title
from infra.repositories.baserepo import BaseRepository
from logic.commands.base import BaseCommand

@dataclass(frozen=True)
class CreateTaskCommand(BaseCommand):
    title: str
    creator_task: User 
    text_task: str
    

@dataclass(frozen=True)
class CreateTaskCommandHandler(BaseCommand):
    repository: BaseRepository
    
    async def handle(self, command: CreateTaskCommand) -> Task:
       
        #TODO чек task на валидность
        title = Title(command.title)
        text_task = Text(command.text_task)
        
        new_task = Task.create_task(created_at=command.creator_task,
                        text_task=text_task,
                        title=title)
        await self.repository.add_task(new_task)
        
        return new_task