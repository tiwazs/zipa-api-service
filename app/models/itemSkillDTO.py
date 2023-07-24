from pydantic import BaseModel
from typing import Optional

class ItemBaseDTO(BaseModel):
    item_id: str
    skill_id: str
    essence_cost: float
    cooldown: float

class ItemCreateDTO(ItemBaseDTO):
    pass

class ItemUpdateDTO(ItemBaseDTO):
    item_id: Optional[str]
    skill_id: Optional[str]
    essence_cost: Optional[float]
    cooldown: Optional[float]

class ItemDTO(ItemBaseDTO):
    id: str
    created_at: str
    updated_at: str
    class Config:
        orm_mode = True
