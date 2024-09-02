import pytest

from domain.entities.messages import Chat
from domain.values.messages import Title
from infra.repositorie.messages import BaseChatRepository
from logic.commands.message import CreateChatCommand
from logic.mediator import Mediator


@pytest.mark.asyncio
async def test_create_chat_succes(
        chat_repository: BaseChatRepository,
        mediator: Mediator,
):
        # TODO: Add faker for generation random tests
        chat: Chat = (await mediator.handle_command(CreateChatCommand(title='gigaTitle')))[0]

        assert await chat_repository.check_chat_exists_by_title(title=chat.title.as_generic_type)


@pytest.mark.asyncio
async def test_create_chat_succes(
        chat_repository: BaseChatRepository,
        mediator: Mediator,
):
        # TODO: Add faker for generation random tests
        chat = Chat(title=Title('gigaChat'))
        chat: Chat = (await mediator.handle_command(CreateChatCommand(title='gigaTitle')))[0]

        assert await chat_repository.check_chat_exists_by_title(title=chat.title.as_generic_type)
