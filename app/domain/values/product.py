from dataclasses import dataclass

from domain.exceptions.product import EmptyTextException, TitleTooLongException, StatusNotDefined
from domain.values.base import BaseValueObject

@dataclass(frozen=True)
class Text(BaseValueObject):
    value: str
    
    def validate(self):
        if not self.value:
            raise EmptyTextException()
    
    def as_generic_type(self) -> str:
        return str(self.value)

@dataclass(frozen=True)
class Title(BaseValueObject):
    value: str
    
    def validate(self):
        if not self.value:
            raise EmptyTextException()
        if len(self.value) > 255:
            raise TitleTooLongException(self.value)
    
    def as_generic_type(self):
        return str(self.value)

@dataclass(frozen=True)
class Status(BaseValueObject):
    value: str
    
    def validate(self):
        if self.value not in ['В работе', 'Cоздана', 'Выполнена']:
            raise StatusNotDefined(self.value)
    
    def as_generic_type(self):
        return str(self.value)
    
    @classmethod
    def at_work(cls) -> str:
        return 'В работе'
    
    @classmethod
    def is_created(cls) -> str:
        return 'Cоздана'
    
    @classmethod
    def is_completed(cls) -> str:
        return 'Выполнена'
    