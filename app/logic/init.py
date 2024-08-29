from functools import lru_cache
from punq import Container, Scope
from domain.entities.product import User
from infra.repositories.baserepo import BaseUserRepository
from infra.repositories.prodrepo import BaseTaskRepository, MemoryTaskRepository, MemoryUserReposiroty
from logic.commands.prodcommand import CreateTaskCommand, CreateTaskCommandHandler, CreateUserCommand, CreateUserCommandHandler, GetUserCommand, GetUserCommandHandler
from logic.mediator import Mediator



@lru_cache(1)
def init_container() -> Container:
    return _init_container()

def _init_container() -> Container:
    container = Container()
    container.register(BaseTaskRepository, MemoryTaskRepository, scope=Scope.singleton)
    container.register(BaseUserRepository, MemoryUserReposiroty, scope=Scope.singleton)
    container.register(CreateTaskCommandHandler)
    container.register(CreateUserCommandHandler)
    container.register(GetUserCommandHandler)
    
    def init_mediator():
        mediator = Mediator()
        mediator.registrer_command(
            CreateTaskCommand,
            [container.resolve(CreateTaskCommandHandler)],
        )
        mediator.registrer_command(
            CreateUserCommand,
            [container.resolve(CreateUserCommandHandler)],
        )
        mediator.registrer_command(
            GetUserCommand,
            [container.resolve(GetUserCommandHandler)],
        )
        return mediator
    
    def init_user():
        """ тест юзер"""
        user = User(
            surname='Айхан',
            name='Амбеков',
            patronymic='Ахмедов',
            mail='ah@test.ru',
        )
        return user
     
    container.register(Mediator, factory=init_mediator)
    container.register(User, factory=init_user)
    
    return container