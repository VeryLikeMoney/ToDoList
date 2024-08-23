from punq import Container, Scope

from infra.repositories.prodrepo import BaseRepository, MemoryRepository
from logic.init import _init_container, init_container

def init_dummy_container() -> Container:
    container = _init_container()
    
    container.register(BaseRepository, MemoryRepository, scope=Scope.singleton)
    return container