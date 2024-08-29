from fastapi.routing import APIRouter
from fastapi.exceptions import HTTPException
from fastapi import Depends, status

from application.api.lists.schema import CreateUserRequestSchema, CreateUserResponseSchema
from application.api.schema import ErrorSchema
from domain.exceptions.base import ApplicationException

from infra.exseptions.prod import User_with_mail_already_exists
from logic.commands.prodcommand import CreateUserCommand
from logic.init import init_container
from logic.mediator import Mediator

router = APIRouter(tags=['User'])

@router.post(
    '/', 
    response_model=CreateUserResponseSchema, 
    status_code=status.HTTP_201_CREATED,
    description='Эндпоинт создает нового пользователя',
    responses={
        status.HTTP_201_CREATED: {'model': CreateUserResponseSchema},
        status.HTTP_400_BAD_REQUEST: {'model': ErrorSchema}
    } 
)
async def create_user_handler(
    schema: CreateUserRequestSchema, 
    container=Depends(init_container)
):
    mediator: Mediator = container.resolve(Mediator)
    try:
        user,*_ = (await mediator.handle_command(CreateUserCommand(
            surname=schema.surname,
            name=schema.name,
            patronymic=schema.patronymic,
            mail=schema.mail,
            department=schema.department,
            phone=schema.phone,
        )))
    except ApplicationException as exception:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail={'error': exception.message})
    return CreateUserResponseSchema.from_entity(user)
