from fastapi import APIRouter
from app.models.item import Item


router = APIRouter(prefix="/items", tags=["items"])

@router.get("/{item_id}", response_model=Item)
async def get_item(item_id: int):
    return Item(id=item_id, name="Widget", price=10.99)