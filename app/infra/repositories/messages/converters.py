from typing import (  # noqa: UP035
    Any,
    Mapping,
)

from domain.entities.messages import (
    Chat,
    ChatListener,
    Message,
)
from domain.values.messages import (
    Text,
    Title,
)


def convert_message_entity_to_document(message: Message) -> dict:
    return {
        'oid': message.oid,
        'text': message.text.as_generic_type(),
        'created_at': message.created_at,
        'chat_oid': message.chat_oid,
    }


def convert_chat_entity_to_document(chat: Chat) -> dict:
    return {
        'oid': chat.oid,
        'title': chat.title.as_generic_type(),
        'created_at': chat.created_at,
    }


def convert_message_document_to_entity(message_document: Mapping[str, Any]) -> Message:
    return Message(
        text=Text(value=message_document['text']),
        oid=message_document['oid'],
        created_at=message_document['created_at'],
        chat_oid=message_document['chat_oid'],
    )


def convert_chat_listener_document_to_entity(listener_id: str) -> ChatListener:
    # TODO: Accept listener entity
    return ChatListener(oid=listener_id)


def convert_chat_document_to_entity(chat_document: Mapping[str, Any]) -> Chat:
    return Chat(
        title=Title(value=chat_document['title']),
        oid=chat_document['oid'],
        created_at=chat_document['created_at'],
        listeners={
            convert_chat_listener_document_to_entity(listener_id=listener_id)
            for listener_id in chat_document.get('listeners', [])
        },
    )
