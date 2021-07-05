from fastapi import APIRouter, WebSocket, WebSocketDisconnect
from starlette.websockets import WebSocketDisconnect
import json

from ....library.ws_connection import ConnectionManager
from ....core.config import settings


# def makeOrder(ticker, amount, orderType, side, price):
#     settings.logger.info(
#         f"NEW ORDER - Ticker: {ticker} - Amount: {amount} - OrderType: {orderType} - Side: {side} - Price: {price}"
#     )


router = APIRouter()

# settings.manager = ConnectionManager()


# @router.websocket("/{client}")
# async def websocket_endpoint(websocket, client: str):
#     await settings.manager.connect(websocket)
#     settings.manager.broadcast("USER_JOIN", f"Client {client} joined.")
#     try:
#         while True:
#             data = await websocket.receive_text()
#             message = json.loads(data)  # CONVIERTE STR A DICT

#             # if message.get("type") is not None:
#             #     if message.get("type").upper() == "ORDER_NEW":
#             #         settings.logger.info("Received: New Order")
#             #         try:
#             #             makeOrder(
#             #                 ticker=message["msg"]["ticker"],
#             #                 amount=message["msg"]["amount"],
#             #                 orderType=message["msg"]["orderType"],
#             #                 side=message["msg"]["side"],
#             #                 price=message["msg"]["price"],
#             #             )
#             #             settings.manager.send_message(
#             #                 f"NEW ORDER - Ticker: {message['msg']['ticker']} - Amount: {message['msg']['amount']} - OrderType: {message['msg']['orderType']} - Side: {message['msg']['side']} - Price: {message['msg']['price']}",
#             #                 websocket,
#             #             )
#             #         except:
#             #             settings.manager.send_message(
#             #                 "No se pudo parsear el mensaje", websocket
#             #             )
#             #     else:
#             #         settings.logger.info("Received: Other")
#             #         settings.logger.info(f"Data sended: {message}")

#             settings.manager.broadcast("BROADCAST_MESSAGE", message)
#     except WebSocketDisconnect:
#         settings.manager.disconnect(websocket)
#         settings.manager.broadcast("USER_LEAVE", f"Client {client} left.")


# @router.websocket("/ws/{client}")
# async def websocket_endpoint(websocket: WebSocket, client: str):
#     await settings.manager.connect(websocket)
#     await settings.manager.broadcast("USER_JOIN", f"Client {client} joined.")
#     try:
#         while True:
#             data = await websocket.receive_text()
#             try:
#                 message = json.loads(data)
#             except:
#                 message = data

#             await settings.manager.broadcast("BROADCAST_MESSAGE", message)
#     except WebSocketDisconnect:
#         settings.manager.disconnect(websocket)
#         await settings.manager.broadcast(
#             "USER_LEAVE", f"Client #{client} left the chat"
#         )
