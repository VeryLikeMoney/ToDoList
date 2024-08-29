from fastapi.routing import APIRouter
from fastapi.exceptions import HTTPException
from fastapi import Depends, status


from application.api.schema import ErrorSchema
from application.api.lists.schema import CreateTaskRequestSchema, CreateTaskResponseSchema
from domain.exceptions.base import ApplicationException
from logic.commands.prod import CreateTaskCommand
from logic.init import init_container
from logic.mediator import Mediator

from domain.entities.product import User

router = APIRouter(tags=['Chat'])

@router.post(
    '/', 
    response_model=CreateTaskResponseSchema, 
    status_code=status.HTTP_201_CREATED,
    description='Эндпоинт создает новый чат, если чат с таким названием существует возвращаяется 400 ошибка',
    responses={
        status.HTTP_201_CREATED: {'model': CreateTaskResponseSchema},
        status.HTTP_400_BAD_REQUEST: {'model': ErrorSchema}
    } 
)
async def create_task_handler(schema: CreateTaskRequestSchema, container=Depends(init_container)):
    mediator: Mediator = container.resolve(Mediator)
    user = container.resolve(User)
    try:
        task,*_ = (await mediator.handle_command(CreateTaskCommand(title=schema.title,creator_task=user,text_task=schema.text_task)))
    except ApplicationException as exception:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail={'error': exception.message})
    return CreateTaskResponseSchema.from_entity(task)