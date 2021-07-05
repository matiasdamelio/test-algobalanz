from fastapi import APIRouter
from .endpoints import prices, websockets

api_router = APIRouter()
api_router.include_router(prices.router, prefix="/prices", tags=["Prices"])
# api_router.include_router(websockets.router, prefix="/ws", tags=["Websocket"])
