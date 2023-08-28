import random

from ..models.unitGenerationDTO import UnitGenerationBaseDTO
#import matplotlib.pyplot as plt


class UnitGenerationService:
    def __init__(self, offset_small:int =5, offset_big:int = 10, growth_rate:float = 0.1, range_small_min:int = 1, range_small_max:int = 9, range_big_min:int = 15, range_big_max:int = 25):
        self.offset_small = offset_small
        self.offset_big = offset_big
        self.growth_rate = growth_rate
        self.range_small_min = range_small_min
        self.range_small_max = range_small_max
        self.range_big_min = range_big_min
        self.range_big_max = range_big_max

    def gaussian_random_in_range(self, start, end, sigma_divider: float = 4):
        """
        Generate a random number between start and end (inclusive)
        following a Gaussian distribution with a mean at the midpoint.
        """

        # Calculate the midpoint (mean) of the range
        mu = (start + end) / 2.0

        # You can adjust sigma based on the desired spread.
        # For example, setting it to (end - start) / 6 makes
        # approximately 99.7% of the numbers fall between start and end
        sigma = (end - start) / sigma_divider

        while True:
            # Generate a Gaussian distributed number with mean=mu and std deviation=sigma
            val = random.gauss(mu, sigma)

            # If the number is within our desired range, return it.
            if start <= val <= end:
                return round(val,1)
            
    def generate_values(self, parameters: dict, sigma_divider: float = 4):
        for key,_ in parameters.items():
            if key == 'vitality' or key == 'essence':
                parameters[key] = self.gaussian_random_in_range(self.range_big_min, self.range_big_max, sigma_divider)
            else:
                parameters[key] = self.gaussian_random_in_range(self.range_small_min, self.range_small_max, sigma_divider)
    
    def generate_unit(self, sigma_divider: float = 4) -> UnitGenerationBaseDTO:
        parameters = {
            'vitality': 0,
            'strength': 0,
            'dexterity': 0,
            'mind': 0,
            'faith': 0,
            'essence': 0,
            'agility': 0,
            'hit_chance': 0,
            'evasion': 0,
        }

        self.generate_values(parameters, sigma_divider)
        return UnitGenerationBaseDTO(**parameters)        

if __name__ == '__main__':
    unit_generation_service  = UnitGenerationService()
    test_values = [ unit_generation_service.gaussian_random_in_range(2, 7) for _ in range(100) ]
    # Organize from smallest to largest
    test_values.sort()

    for val in test_values:
        print(val)

    # Plot the distribution of the numbers generated
    #plt.plot(test_values)
    #plt.show()