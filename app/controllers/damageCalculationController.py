from typing import List, Optional
from fastapi import APIRouter, Form, Request, Response

from ..models.damageCalculationDTO import DamageCalculationDTO

from ..services.damageCalculationService import DamageCalculatorService

router = APIRouter(prefix="/damage_calculation", tags=["Damage Calculation"])

msg_not_found = 'Trait not found'

@router.post("/")
async def calculate(damage_options: DamageCalculationDTO,
                    shield: float = 0, 
                    armor_penetration: float = 0, 
                    is_projectile:bool = False, 
                    block_reduction:float=50,
                    deflect_reduction:float=50,
                    type_modifier: float = None,
                    only_final_damage: Optional[bool] = False):
    damage = damage_options.damage
    hit_chance = damage_options.hit_chance
    armor = damage_options.armor
    evasion = damage_options.evasion
    damage_modifiers = damage_options.damage_modifiers if damage_options.damage_modifiers else []

    if only_final_damage:
        final_damage,_= DamageCalculatorService().damage_calculation(damage, hit_chance, armor, evasion, damage_modifiers, shield, armor_penetration, is_projectile, block_reduction, deflect_reduction, type_modifier)
        return final_damage
    else:
        _,final_damage_diict = DamageCalculatorService().damage_calculation(damage, hit_chance, armor, evasion, damage_modifiers, shield, armor_penetration, is_projectile, block_reduction, deflect_reduction, type_modifier)
        return final_damage_diict