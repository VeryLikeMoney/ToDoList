from dataclasses import dataclass

from domain.exceptions.base import ApplicationException

@dataclass(eq=False)
class BaseRepositoryException(ApplicationException):
    
    @property
    def message(self):
        return 'Ошибка взамодейсвтия репозитория'