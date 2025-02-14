from collections.abc import Iterable
from dataclasses import dataclass

from domain.entities.messages import (
    Chat,
    ChatListener,
    Message,
)
from infra.repositories.filters.messages import (
    GetAllChatsFilters,
    GetMessagesFilters,
)
from infra.repositories.messages.base import (
    BaseChatsRepository,
    BaseMessagesRepository,
)
from logic.exceptions.messages import ChatNotFoundException
from logic.queries.base import (
    BaseQuery,
    BaseQueryHandler,
)


@dataclass(frozen=True)
class GetChatDetailQuery(BaseQuery):
    chat_oid: str


@dataclass(frozen=True)
class GetMessagesQuery(BaseQuery):
    chat_oid: str
    filters: GetMessagesFilters


@dataclass(frozen=True)
class GetAllChatsQuery(BaseQuery):
    filters: GetAllChatsFilters


@dataclass(frozen=True)
class GetAllChatsListenerQuery(BaseQuery):
    chat_oid: str


@dataclass(frozen=True)
class GetChatDetailQueryHandler(BaseQueryHandler):
    chats_repository: BaseChatsRepository
    message_repository: BaseMessagesRepository  # Todo: Take message separately

    async def handle(self, query: GetChatDetailQuery) -> Chat:
        chat = await self.chats_repository.get_chat_by_oid(oid=query.chat_oid)

        if not chat:
            raise ChatNotFoundException(chat_oid=query.chat_oid)

        return chat


@dataclass(frozen=True)
class GetMessagesQueryHandler(BaseQueryHandler):
    messages_repository: BaseMessagesRepository

    async def handle(self, query: GetMessagesQuery) -> tuple[Iterable[Message], int]:
        return await self.messages_repository.get_messages(
            chat_oid=query.chat_oid,
            filters=query.filters,
        )


@dataclass(frozen=True)
class GetAllChatsQueryHandler(BaseQueryHandler[GetAllChatsQuery, Iterable[Chat]]):
    chat_repository: BaseChatsRepository

    async def handle(self, query: GetAllChatsQuery) -> Iterable[Chat]:  # type: ignore
        return await self.chat_repository.get_all_chats(filters=query.filters)


@dataclass(frozen=True)
class GetAllChatsListenerQueryHandler(BaseQueryHandler[GetAllChatsListenerQuery, Iterable[ChatListener]]):
    chats_repository: BaseChatsRepository

    async def handle(self, query: GetAllChatsListenerQuery) -> ChatListener:
        # TODO: delete two requests
        chat = await self.chats_repository.get_chat_by_oid(oid=query.chat_oid)

        if not chat:
            raise ChatNotFoundException(chat_oid=query.chat_oid)

        return await self.chats_repository.get_all_chat_listeners(chat_oid=query.chat_oid)
