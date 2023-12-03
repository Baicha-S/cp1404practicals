"""Quik Picks Program"""
import random

MINIMUM_NUMBER = 1
MAXIMUM_NUMBER = 45
NUMBERS_PER_LINE = 6

quik_pick = int(input("How many quik picks? "))

for i in range(quik_pick):
    quik_picks = []
    for j in range(NUMBERS_PER_LINE):
        number = random.randint(MINIMUM_NUMBER, MAXIMUM_NUMBER)
        while number in quik_picks:  # Check repeated number
            number = random.randint(MINIMUM_NUMBER, MAXIMUM_NUMBER)
        quik_picks.append(number)
    quik_picks.sort()
    print(" ".join(f"{number:2}" for number in quik_picks))
