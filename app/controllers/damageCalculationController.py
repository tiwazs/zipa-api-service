from typing import Optional
from fastapi import APIRouter, Form, Request, Response

from ..services.damageCalculationService import DamageCalculatorService

router = APIRouter(prefix="/damage_calculation", tags=["Damage Calculation"])

msg_not_found = 'Trait not found'

@router.post("/")
async def calculate(request: Request, 
                    response: Response, 
                    damage: float = Form(...), 
                    hit_chance: float = Form(...), 
                    armor: float = Form(...), 
                    evasion: float = Form(...), 
                    shield: float = 0, 
                    armor_penetration: float = 0, 
                    is_projectile:bool = False, 
                    block_reduction:float=50,
                    deflect_reduction:float=50, 
                    type_modifier: float = None,
                    only_final_damage: Optional[bool] = False):
    if only_final_damage:
        final_damage,_= DamageCalculatorService().damage_calculation(damage, hit_chance, armor, evasion, shield, armor_penetration, is_projectile, block_reduction, deflect_reduction, type_modifier)
        return final_damage
    else:
        _,final_damage_diict = DamageCalculatorService().damage_calculation(damage, hit_chance, armor, evasion, shield, armor_penetration, is_projectile, block_reduction, deflect_reduction, type_modifier)
        return final_damage_diict