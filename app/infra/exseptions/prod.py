from dataclasses import dataclass

from infra.exseptions.base import BaseRepositoryException

@dataclass(eq=False)
class User_with_mail_already_exists(BaseRepositoryException):
    mail: str
    
    @property
    def message(self):
        return f'Пользователь c {self.mail} почтой уже существует'
    