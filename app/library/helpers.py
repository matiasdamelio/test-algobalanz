import os
import markdown
import pickle
import asyncio
from itertools import cycle
import random
from ..core.config import settings


def openfile(filename):
    filepath = os.path.join("app/pages/", filename)
    with open(filepath, "r", encoding="utf-8") as input_file:
        text = input_file.read()

    html = markdown.markdown(
        text, extensions=["nl2br", "tables", "md_in_html", "codehilite", "sane_lists"]
    )
    data = {"text": html}
    return data


def load_object(filename):
    try:
        with open(filename, "rb") as f:
            return pickle.load(f)
    except Exception as ex:
        print("Error during unpickling object (Possibly unsupported):", ex)


async def socketSimulado():
    for index, data in enumerate(cycle(settings.data)):
        settings.iterator = index
        yield data
        await asyncio.sleep(round(random.uniform(0, 0.2), 3))


async def consume():
    async for message in socketSimulado():
        await message_handler(message)


async def message_handler(msg):
    settings.market_data[msg["securityID"]] = msg
    try:
        await settings.manager.broadcast(
            "BROADCAST_MESSAGE", settings.market_data[msg["securityID"]]
        )
    except:
        pass
