"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""
import random
MINIMUM_SCORE = 0
MAXIMUM_SCORE = 100
EXCELLENT_THRESHOLD = 90
PASSABLE_THRESHOLD = 50


def main():
    """Get user's score and print score result and random score result."""
    score = float(input("Enter score: "))
    print(determine_score(score))
    random_score = random.randint(MINIMUM_SCORE, MAXIMUM_SCORE)
    print(f"Random score is {random_score}, which is {determine_score(random_score)}.")


def determine_score(score):
    """Determine the result based on the score."""
    if MINIMUM_SCORE > score or score > MAXIMUM_SCORE:
        return "Invalid score"
    elif score >= EXCELLENT_THRESHOLD:
        return "Excellent"
    elif score >= PASSABLE_THRESHOLD:
        return "Passable"
    else:
        return "Bad"


main()
