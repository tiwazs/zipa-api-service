import random
#import matplotlib.pyplot as plt


class UnitGenerationService:
    def __init__(self, offset_small:int =5, offset_big:int = 10, growth_rate:float = 0.1):
        self.offset_small = offset_small
        self.offset_big = offset_big
        self.growth_rate = growth_rate

    def gaussian_random_in_range(self, start, end, sigma_divider: float = 6):
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