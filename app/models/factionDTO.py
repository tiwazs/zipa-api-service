from pydantic import BaseModel
from typing import Optional

class FactionBaseDTO(BaseModel):
    name: str
    description: str
    identity: Optional[str] = None
    aspects: Optional[str] = None
    
class FactionCreateDTO(FactionBaseDTO):
    pass

class FactionUpdateDTO(FactionBaseDTO):
    name: Optional[str] = None
    description: Optional[str] = None
    identity: Optional[str] = None
    aspects: Optional[str] = None

class FactionDTO(FactionBaseDTO):
    id: int
    class Config:
        orm_mode = True

