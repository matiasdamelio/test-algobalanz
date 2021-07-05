from fastapi import APIRouter
from ....core.config import settings

router = APIRouter()


@router.get("/")
async def prices():
    return settings.market_data


@router.get("/iterator")
async def iterator():
    return {"response": settings.iterator}


@router.get("/security_id")
async def get_securities():
    return {"response": sorted(set(settings.market_data.keys()))}


@router.get("/security_id/{security_id}")
async def get_prices(security_id):
    if security_id not in settings.market_data.keys():
        return {"response": f"SecurityID {security_id} not in Market Data"}
    return {"response": settings.market_data[security_id]}
