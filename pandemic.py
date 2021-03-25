from scipy.stats import norm
import random
import time

# Create a person class to simulate one person
class Person:
    def __init__(self, starting_immunity):
        if random.randint(0, 100) < starting_immunity:
            self.immunity = True
        else:
            self.immunity = False
        self.cantagiousness = 0
        self.mask = False
        self.contagious_days = 0
        # Gaussian distribution for number of friends (average is 5 friends)
        self.friends = int((norm.rvs(size=1, loc=0.5, scale=0.15) * 10).round(0))

        def wear_mask(self):
            self.contagiousness = self.contagiousness / 2
