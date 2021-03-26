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

    @staticmethod
    def initiateSim():
        num_people = int(input("Population: "))
        starting_immunity = int(input("Percentage of people with natural immunity: "))
        starting_infecters = int(input("How many people will be contagious on day 1: "))

        for x in range(0, num_people):
            people_dict.append(Person(starting_immunity))
        for x in range(0, starting_infecters):
            people_dict[random.randint(0, len(people_dict) - 1)].contagiousness = int(
                (norm.rvs(size=1, loc=0.5, scale=0.15)[0] * 10).round(0) * 10
            )
        days_contagious = int(input("How many days contagious: "))
        lockdown_day = int(input("After what day should lockdown be enforced: "))
        mask_day = int(input("What day do masks begin to be worn: "))
        return days_contagious, lockdown_day, mask_day
