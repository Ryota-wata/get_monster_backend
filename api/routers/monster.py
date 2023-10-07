from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from api.models.monster import Monster
import api.cruds.monster as monster_crud
from api.db import get_db

import api.schemas.monster as monster_schema

router = APIRouter()

@router.get("/monsters", response_model=list[monster_schema.Monster])
async def get_monsters(db: AsyncSession = Depends(get_db)):
    stmt = select(Monster)
    result = await db.execute(stmt)
    return result.scalars().all()


@router.post("/catch_monster")
async def catch_monster(monster: monster_schema.Monster, db: AsyncSession = Depends(get_db)):
    result = await monster_crud.catching_monster(db, monster)
    return result
