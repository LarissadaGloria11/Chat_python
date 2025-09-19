#app/router/websocket

from fastapi import APIRouter, WebSocket
from ..manager import manager
from ..database import salvar_mensagem

router = APIRouter()

@router.websocket("/ws/{sala_id}")
async def websocket_endpoint(websocket: WebSocket, sala_id:str, nickname: str = "Anõnimo"):
    await manager.concect(sala_id, websocket, nickname)

    while True:
        data = await websocket.receive_text()

        await salvar_mensagem(sala_id, nickname, data)

        #broadcast 