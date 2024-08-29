import pytest

from faker import Faker
from domain.entities.product import Task, User
from domain.values.product import Text, Title
from infra.repositories.prodrepo import BaseTaskRepository
from logic.commands.prod import CreateTaskCommand
from logic.mediator import Mediator

@pytest.mark.asyncio
async def test_create_chat_command_success(
    chat_repository: BaseTaskRepository,
    mediator: Mediator,
    faker: Faker,
):
    title: str = faker.text()[:255]
    creator_task: User = User(
        surname='Степан',
        name='Степа',
        patronymic='Степов',
        mail='st@fakemail.ru'
    )
    text: Text = Text(faker.text())
    task: Task
    task, *_ = (await mediator.handle_command(CreateTaskCommand(
        title=title,
        creator_task=creator_task,
        text_task=text
        )))
    assert await chat_repository.check_task_exists_by_oid(oid_task=task.oid)