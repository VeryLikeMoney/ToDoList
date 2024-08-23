from datetime import datetime
import pytest

from faker import Faker

from domain.entities.product import Task, User
from domain.values.product import Text, Title, Status

def test_create_task_succes():
    user = User(
        surname='Степан',
        name='Степа',
        patronymic='Степов',
        mail='st@fakemail.ru'
    )
    text_task = Text('Тест')
    title = Title('Тайтл тест')
    task: Task = Task.create_task(
        creator_task=user,
        text_task=text_task,
        title=title
    )
    assert task.created_at.date() == datetime.today().date()
    assert task.status == Status(Status.is_created())
    