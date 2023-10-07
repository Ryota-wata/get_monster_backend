from sqlalchemy import select
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession

import api.models.monster as monster_model
import api.schemas.monster as monster_schema

async def catching_monster(db: AsyncSession, monster: monster_schema.Monster):
    stmt = select(monster_model.Monster).where(monster_model.Monster.name == monster.name)
    result = await db.execute(stmt)
    existing_monster = result.scalars().first()
    
    if existing_monster:
        return {"success": False}
    else:
        monster = monster_model.Monster(**monster.dict())
        db.add(monster)
        await db.commit()
        await db.refresh(monster)
        return {"success": True}


async def get_monsters(db: AsyncSession) -> list[tuple[int, str]]:
  result: Result = await db.execute()
  return result.scalars().first()
