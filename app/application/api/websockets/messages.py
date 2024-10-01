from fastapi.routing import APIRoute
from fastapi.websockets import WebSocket


router = APIRoute(
    tags=["chats"],
)


@router.websocket('{chat_oid}')
async def messages_handler(chat_oid: str, websocket: WebSocket):
    await websocket.accept()
