from typing import List
from fastapi import WebSocket
from ..core.config import settings


class ConnectionManager:
    def __init__(self):
        self.active_connections: List[WebSocket] = []
        print("Websocket opened")

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)

    def disconnect(self, websocket: WebSocket):
        self.active_connections.remove(websocket)

    async def send_message(self, message: str, websocket: WebSocket):
        await websocket.send_json({"type": "MESSAGE", "msg": message})

    async def broadcast(self, type: str, message: dict):
        for connection in self.active_connections:
            await connection.send_json({"type": type, "msg": message})
