from pydantic import BaseModel

class Monster(BaseModel):
  id: int
  name: str

  class Config:
    orm_mode = True