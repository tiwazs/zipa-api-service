from pydantic import BaseModel
from typing import Optional

class ItemSkillBaseDTO(BaseModel):
    item_id: str
    skill_id: str
    essence_cost: str
    vitality_cost: str
    cooldown: str

class ItemSkillCreateDTO(ItemSkillBaseDTO):
    pass

class ItemSkillUpdateDTO(ItemSkillBaseDTO):
    essence_cost: Optional[str]
    vitality_cost: Optional[str]
    cooldown: Optional[str]

class ItemSkillDTO(ItemSkillBaseDTO):
    id: str
    created_at: str
    updated_at: str
    class Config:
        orm_mode = True
