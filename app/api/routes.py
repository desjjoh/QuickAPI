from fastapi import APIRouter
from app.models.item import Item
from app.core.logging import log

router = APIRouter(prefix="/items", tags=["items"])

@router.get("/{item_id}", response_model=Item)
async def get_item(item_id: int):
    log.info("get_item_called", item_id=item_id)
    return Item(id=item_id, name="Widget", price=10.99)