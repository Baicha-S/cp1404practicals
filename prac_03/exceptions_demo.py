"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
When user input string to numerator and denominator.

2. When will a ZeroDivisionError occur?
When user input 0 to denominator.

3. Could you change the code to avoid the possibility of a ZeroDivisionError?
Yes, by using while loop until user input is not equal to 0.
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    while denominator == 0:  # avoid possible 0 as a denominator
        print("Cannot divide by zero!")
        denominator = int(input("Enter the denominator: "))

    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")
