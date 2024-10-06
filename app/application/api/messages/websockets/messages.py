from uuid import UUID
from fastapi import Depends
from punq import Container

from fastapi.routing import APIRouter
from fastapi.websockets import WebSocket

from application.api.common.websockets.managers import BaseConnectionManager, ConnectionManager
from infra.message_brokers.base import BaseMessageBroker
from logic.init import init_container
from settings.config import Config


router = APIRouter(
    tags=["chats"],
)


@router.websocket('/{chat_oid}/')
async def messages_handler(
    chat_oid: UUID,
    websocket: WebSocket,
    container: Container = Depends(init_container),
):
    config: Config = container.resolve(Config)
    connection_manager: BaseConnectionManager = container.resolve(BaseConnectionManager)

    await connection_manager.accept_connection(websocket=websocket, key=chat_oid)

    message_broker: BaseMessageBroker = container.resolve(BaseMessageBroker) 

    try:
        async for message in message_broker.start_consuming(
            topic=config.new_message_received_topic,
        ):
            await connection_manager.send_all(key=chat_oid, json_message=message)
    finally:
        await connection_manager.remove_connection(websocket=websocket, key=chat_oid)
        await message_broker.stop_consuming()
        g
    await message_broker.stop_consuming()
    await websocket.close(reason="Zaebal")
