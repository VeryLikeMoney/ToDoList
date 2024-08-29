from pydantic import BaseModel

from domain.entities.product import Task, User

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

class CreateUserRequestSchema(BaseModel):
    surname: str
    name: str
    patronymic: str
    mail: str
    department: str 
    phone: str 
    
class CreateUserResponseSchema(BaseModel):
    oid: str
    fullname: str
    mail: str
    department: str
    phone: str
    
    @classmethod
    def from_entity(cls, user: User) -> 'CreateUserResponseSchema':
        return CreateUserResponseSchema(
            oid=user.oid,
            fullname=user.fullname,
            mail=user.mail,
            department=user.department,
            phone=user.phone, 
        )
