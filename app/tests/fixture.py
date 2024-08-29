from punq import Container, Scope

from infra.repositories.prodrepo import BaseTaskRepository, MemoryTaskRepository
from logic.init import _init_container, init_container

def init_dummy_container() -> Container:
    container = _init_container()
    
    container.register(BaseTaskRepository, MemoryTaskRepository, scope=Scope.singleton)
    return container