from pydantic import BaseModel
from typing import Optional

class ItemTraitBaseDTO(BaseModel):
    item_id: str
    trait_id: str
    conditions: Optional[str]

class ItemTraitCreateDTO(ItemTraitBaseDTO):
    pass

class ItemTraitUpdateDTO(ItemTraitBaseDTO):
    item_id: Optional[str]
    trait_id: Optional[str]
    conditions: Optional[str]

class ItemTraitDTO(ItemTraitBaseDTO):
    id: str
    created_at: str
    updated_at: str
    class Config:
        orm_mode = True