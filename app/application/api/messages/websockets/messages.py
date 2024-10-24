from fastapi import (
    Depends,
    WebSocketDisconnect,
)
from fastapi.routing import APIRouter
from fastapi.websockets import WebSocket

from punq import Container

from infra.websockets.managers import BaseConnectionManager
from logic.init import init_container


router = APIRouter(
    tags=["chats"],
)


@router.websocket('/{chat_oid}/')
async def messages_handler(
    chat_oid: str,
    websocket: WebSocket,
    container: Container = Depends(init_container),
):
    connection_manager: BaseConnectionManager = container.resolve(BaseConnectionManager)
    # TODO: Check if chat exists before connecting
    await connection_manager.accept_connection(websocket=websocket, key=chat_oid)

    await websocket.send_text("You are connected!")

    try:
        while True:
            await websocket.receive_text()

    except WebSocketDisconnect:
        await connection_manager.remove_connection(websocket=websocket, key=chat_oid)
