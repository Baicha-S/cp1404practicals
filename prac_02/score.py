"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""
import random


def main():
    score = float(input("Enter score: "))
    result = determine_score(score)
    print(result)


def determine_score(score):
    if 0 <= score <= 100:
        if score >= 90:
            return "Excellent"
        elif score >= 50:
            return "Passable"
        else:
            return "Bad"


def generate_random_score():
    score = random.randint(0, 100)
    result = determine_score(score)
    print(result)


main()
generate_random_score()
