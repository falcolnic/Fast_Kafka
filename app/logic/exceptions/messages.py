from dataclasses import dataclass

from logic.exceptions.base import LogicException



@dataclass(eq=False)
class ChatWithThatTitleAlreadyExistsException(LogicException):
    title: str


    @property
    def message(self):
        return f"Chat with name {self.title} already exist"

@dataclass(eq=False)
class ChatNotFoundException(LogicException):
    chat_oid: str

    @property
    def message(self):
        return f"Chat with this OID {self.chat_oid} not found"