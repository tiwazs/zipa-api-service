import random
import re
from typing import List

import matplotlib.pyplot as plt
import functools

class DamageCalculatorService:
    def weighted_random(self, options):
        weights = [options[0]]

        for i in range(1, len(options)):
            weights.append(weights[i-1] + options[i])
        
        rand = random.uniform(0, weights[-1])

        for i in range(len(weights)):
            if rand < weights[i]:
                return i
    
    def apply_modifiers(self, damage: float, modifiers: List[str]):
        if modifiers is None: return damage
        for modifier in modifiers:
            regex = '(?P<sign>[+-])?(?P<value>([\d+.]+|ND|MD|HP))?(?P<porcentage>\s*%)?(?P<max>\s*max)?'
            match = re.search(regex, modifier)
            sign = match['sign']
            value = match['value']
            porcentage = match['porcentage']

            if(porcentage and sign == '+'):
                damage += damage * (float(value) / 100)
            elif(porcentage and sign == '-'):
                damage -= damage * (float(value) / 100)
            elif(sign == '+'):
                damage += float(value)
            elif(sign == '-'):
                damage -= float(value)
            elif(porcentage):
                damage = damage * (float(value) / 100)
        

        return damage
    
    def hit_evasion(self, hit_chance: float, evasion: float, hw: float=1, offset: float=25) -> List[float]:
        base_hit_probability = offset + ( (hit_chance*hw) / (hit_chance*hw + evasion) )*100
        base_hit_probability = base_hit_probability if base_hit_probability <= 100 else 100
        base_evasion_probability = 100 - base_hit_probability

        critical_probability = base_hit_probability*0.2
        hit_probability = base_hit_probability*0.8
        deflect_probability = base_evasion_probability*0.5
        evasion_probability = base_evasion_probability*0.5

        return [critical_probability, hit_probability, deflect_probability, evasion_probability]
    
    def damage_calculation(self, damage: float, 
                                 hit_chance: float,
                                 armor: float, 
                                 evasion: float,
                                 damage_modifiers: List[str] = None, 
                                 shield: float = 0,
                                 armor_penetration: float = 0, 
                                 is_projectile:bool = False, 
                                 block_reduction:float=50,
                                 deflect_reduction:float=50, 
                                 type_modifier: float = None):
        hit_evasion_types = ['critical', 'hit', 'deflect', 'evasion']
        block_types = ['hit', 'blocked']

        block_reduction = 1-block_reduction/100
        deflect_reduction = 1-deflect_reduction/100

        damage_after_modifiers = self.apply_modifiers(damage, damage_modifiers) if damage_modifiers else damage

        damage_calculation_dict = {
            'damage': damage,
            'damage_modifiers': damage_modifiers if damage_modifiers else [],
            'damage_after_modifiers': damage_after_modifiers,
            'hit_chance': hit_chance,
            'armor': armor,
            'evasion': evasion,
            'shield': shield,
            'armor_penetration': armor_penetration,
            'is_projectile': is_projectile,
            'block_reduction': block_reduction,
            'deflect_reduction': deflect_reduction,
            'type_modifier': type_modifier,
            'result_details': {
                'block_probability': 0,
                'block_result': "hit",
                'damage_after_block': 0,
                'critical_probability': 0,
                'hit_probability': 0,
                'deflect_probability': 0,
                'evasion_probability': 0,
                'hit_evasion_result': 0,
                'damage_after_hit_evasion': 0,
                'armor': 0,
                'damage_after_base_armor': 0,
                'armor_after_armor_penetration': 0,
                'damage_after_total_armor': 0,
            },
            'final_damage': 0
        }

        if type_modifier is None:
            pass
        
        final_damage = damage_after_modifiers

        # Evaluate if its blocked if its projectile
        block_result = 0
        if is_projectile and shield > 0:

            damage_calculation_dict['result_details']['block_probability'] = shield

            # Evaluate if its blocked. shield is the probability of blocking
            shield_block_probabilities = [100-shield, shield]
            block_result = self.weighted_random(shield_block_probabilities)

            damage_calculation_dict['result_details']['block_result'] = block_types[block_result]
            # If its blocked, reduce it by half
            if block_result == 1:
                damage_calculation_dict['result_details']['damage_after_block'] = final_damage*block_reduction
                
        
        # Determine probability to hit normally, critically, deflect or evade
        hit_evasion_probabilities = self.hit_evasion(hit_chance, evasion)
        damage_calculation_dict['result_details']['critical_probability'] = hit_evasion_probabilities[0]
        damage_calculation_dict['result_details']['hit_probability'] = hit_evasion_probabilities[1]
        damage_calculation_dict['result_details']['deflect_probability'] = hit_evasion_probabilities[2]
        damage_calculation_dict['result_details']['evasion_probability'] = hit_evasion_probabilities[3]

        # Evualate if it hits normally, critically, deflects or evades
        hit_evasion_result = self.weighted_random(hit_evasion_probabilities)
        damage_calculation_dict['result_details']['hit_evasion_result'] = hit_evasion_types[hit_evasion_result]

        # Critical hit
        if hit_evasion_result == 0:
            final_damage = final_damage*1.8
        # Normal hit
        elif hit_evasion_result == 1:
            pass
        # Deflected
        elif hit_evasion_result == 2:
            pass
        # Evaded
        elif hit_evasion_result == 3:
            final_damage = 0

        # Apply deflect Or Block depending on the biggest reduction
        if block_result == 1 and hit_evasion_result != 2:
            final_damage = final_damage*block_reduction
        elif block_result != 1 and hit_evasion_result == 2:
            final_damage = final_damage*deflect_reduction
        elif block_result == 1 and hit_evasion_result == 2:
            min_reduction = min(block_reduction, deflect_reduction)
            final_damage = final_damage*min_reduction
        
        damage_calculation_dict['result_details']['damage_after_hit_evasion'] = final_damage

        # Determine damage redtuction after base armor. only for view purposes
        armor = armor*5
        damage_calculation_dict['result_details']['armor'] = armor
        damage_calculation_dict['result_details']['damage_after_base_armor'] = final_damage - final_damage*(armor/100)

        # Apply armor penetration
        armor = armor - (armor*armor_penetration/100)
        damage_calculation_dict['result_details']['armor_after_armor_penetration'] = armor

        # Apply armor reduction
        final_damage = final_damage - final_damage*(armor/100)
        damage_calculation_dict['result_details']['damage_after_total_armor'] = final_damage

        damage_calculation_dict['final_damage'] = final_damage
        return final_damage, damage_calculation_dict

if __name__ == '__main__':
    options = [10,50,20,15,5]
    test_values = [ DamageCalculatorService().weighted_random(options) for _ in range(1000) ]
    options_sum = [ 0 for _ in range(len(options)) ]
    
    for option_id in range(len(options_sum)):
        options_sum[option_id] = functools.reduce( lambda acc, idx: acc+1 if idx==option_id else acc, test_values,  0)

    print(options_sum)