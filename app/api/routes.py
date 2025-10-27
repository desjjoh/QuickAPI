from typing import List

from fastapi import APIRouter, Depends, HTTPException, status

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from app.models.item import Item
from app.models.db_models import ItemORM
from app.models.schemas import ItemIn, ItemOut
from app.core.logging import log
from app.services.db import get_session

router = APIRouter(prefix="/items", tags=["items"])

@router.post("/", response_model=ItemOut, status_code=status.HTTP_201_CREATED)
async def create_item(payload: ItemIn, db: AsyncSession = Depends(get_session)):
    item = ItemORM(name=payload.name, price=payload.price)
    db.add(item)
    await db.commit()
    await db.refresh(item)
    log.info("item_created", id=item.id, name=item.name, price=item.price)
    return ItemOut(id=item.id, name=item.name, price=item.price)

@router.get("/{item_id}", response_model=ItemOut)
async def get_item(item_id: int, db: AsyncSession = Depends(get_session)):
    res = await db.execute(select(ItemORM).where(ItemORM.id == item_id))
    obj = res.scalar_one_or_none()
    if not obj:
        raise HTTPException(status_code=404, detail="Item not found")
    return ItemOut(id=obj.id, name=obj.name, price=obj.price)

@router.get("/", response_model=List[ItemOut])
async def list_items(db: AsyncSession = Depends(get_session)):
    res = await db.execute(select(ItemORM).order_by(ItemORM.id))
    items = res.scalars().all()
    return [ItemOut(id=i.id, name=i.name, price=i.price) for i in items]