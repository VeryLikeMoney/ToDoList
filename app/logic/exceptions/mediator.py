from dataclasses import dataclass

from logic.exceptions.base import LogicException



@dataclass(eq=False)
class CommandHandlersNotRegisteredException(LogicException):
    command_type : type
    
    @property
    def messsage(self):
        return f'Не удалось найти обрабодчики для команды: {self.command_type}'