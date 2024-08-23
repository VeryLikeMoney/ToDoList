from pytest import fixture

from punq import Container
from infra.repositories.prodrepo import BaseRepository
from logic.mediator import Mediator
from tests.fixture import init_dummy_container

@fixture(scope='function')
def container() -> Container:
    return init_dummy_container()

@fixture()
def mediator(container: Container) -> Mediator:
    return container.resolve(Mediator)

@fixture()
def chat_repository(container: Container) -> BaseRepository:
    return container.resolve(BaseRepository)