"""UnreliableCar Class"""
import random

from prac_09.car import Car


class UnreliableCar(Car):
    """An unreliability version of car."""

    def __init__(self, name, fuel, reliability):
        """Initialise an UnreliableCar."""
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        """Drive the car when random number is less than car's reliability. """
        random_number = random.uniform(1, 100)
        if random_number < self.reliability:
            distance_driven = super().drive(distance)
        else:
            distance_driven = super().drive(0)
        return distance_driven
