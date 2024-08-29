from pydantic import BaseModel

from domain.entities.product import Task

class CreateTaskRequestSchema(BaseModel):
    title: str
    text_task: str

class CreateTaskResponseSchema(BaseModel):
    oid: str
    title: str
    text_task: str
    user: dict
    
    @classmethod
    def from_entity(cls, task: Task) -> 'CreateTaskResponseSchema':
        return CreateTaskResponseSchema(
            oid=task.oid,
            title=task.title.as_generic_type(),
            text_task=task.text_task.as_generic_type(),
            user={
                'surname': task.creator_task.surname,
                'name': task.creator_task.name,
                'patronymic': task.creator_task.patronymic,
                'mail': task.creator_task.mail,
            }
        )