from functools import lru_cache
from punq import Container, Scope
from infra.repositories.prodrepo import BaseRepository, MemoryRepository
from logic.commands.product import CreateTaskCommand, CreateTaskCommandHandler
from logic.mediator import Mediator


@lru_cache(1)
def init_container():
    return _init_container()

def _init_container() -> Container:
    container = Container()
    container.register(BaseRepository, MemoryRepository, scope=Scope.singleton)
    container.register(CreateTaskCommandHandler)
    
    def init_mediator():
        mediator = Mediator()
        mediator.registrer_command(
            CreateTaskCommand,
            [container.resolve(CreateTaskCommandHandler)],
        )
        return mediator
    
    container.register(Mediator, factory=init_mediator)
    
    return container