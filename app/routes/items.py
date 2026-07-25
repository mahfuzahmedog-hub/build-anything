"""Item API routes."""

from datetime import datetime

from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel, field_serializer
from sqlalchemy.orm import Session

from app.database import get_db
from app.models import Item

router = APIRouter(prefix="/api/items", tags=["items"])


class ItemCreate(BaseModel):
    title: str
    description: str = ""


class ItemResponse(BaseModel):
    id: int
    title: str
    description: str
    created_at: datetime

    model_config = {"from_attributes": True}

    @field_serializer("created_at")
    def serialize_dt(self, dt: datetime) -> str:
        return dt.isoformat()


@router.get("")
async def list_items(db: Session = Depends(get_db)):  # noqa: B008
    items = db.query(Item).order_by(Item.created_at.desc()).all()
    return [ItemResponse.model_validate(i) for i in items]


@router.post("", status_code=201)
async def create_item(item: ItemCreate, db: Session = Depends(get_db)):  # noqa: B008
    db_item = Item(title=item.title, description=item.description)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return ItemResponse.model_validate(db_item)


@router.delete("/{item_id}")
async def delete_item(item_id: int, db: Session = Depends(get_db)):  # noqa: B008
    db_item = db.query(Item).filter(Item.id == item_id).first()
    if not db_item:
        raise HTTPException(status_code=404, detail="Item not found")
    db.delete(db_item)
    db.commit()
    return {"ok": True}
