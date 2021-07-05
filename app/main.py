from fastapi import FastAPI, Request, WebSocket, WebSocketDisconnect
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

# from itertools import cycle
import asyncio
import json
import websockets

from starlette import websockets
from app.routers import unsplash, twoforms, accordion
from .library.helpers import *
from .core.config import settings
from .api.v1.api import api_router

from .library.ws_connection import ConnectionManager

app = FastAPI(
    title=settings.PROJECT_NAME,
    openapi_url=f"{settings.API_V1_STR}/openapi.json",
)

templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

# app.include_router(unsplash.router)
# app.include_router(twoforms.router)
# app.include_router(accordion.router)
app.include_router(api_router, prefix=settings.API_V1_STR)


@app.on_event("startup")
async def startup_event():
    settings.data = load_object("data/data.pickle")
    settings.manager = ConnectionManager()
    asyncio.create_task(consume())


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    data = openfile("home.md")
    return templates.TemplateResponse("page.html", {"request": request, "data": data})


# @app.get("/page/{page_name}", response_class=HTMLResponse)
# async def page(request: Request, page_name: str):
#     data = openfile(page_name + ".md")
#     return templates.TemplateResponse("page.html", {"request": request, "data": data})


@app.websocket("/ws/{client}")
async def websocket_endpoint(websocket: WebSocket, client: str):
    await settings.manager.connect(websocket)
    # await settings.manager.broadcast("USER_JOIN", f"Client {client} joined.")
    try:
        while True:
            data = await websocket.receive_text()
            try:
                message = json.loads(data)
            except:
                message = data

            # await settings.manager.broadcast("BROADCAST_MESSAGE", message)
    except WebSocketDisconnect:
        settings.manager.disconnect(websocket)
        await settings.manager.broadcast(
            "USER_LEAVE", f"Client #{client} left the chat"
        )
