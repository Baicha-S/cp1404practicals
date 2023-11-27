import random

print(random.randint(5, 20))  # line 1
print(random.randrange(3, 10, 2))  # line 2
print(random.uniform(2.5, 5.5))  # line 3

"""
1. What did you see on line 1?
The smallest number was 5, and the largest was 20

2. What did you see on line 2?
The smallest number was 3, and the largest was 9

3. What did you see on line 3?
The smallest number was 2.5, and the largest was 5.5

4. Write code, not a comment, to produce a random number between 1 and 100 inclusive.
"""

print(random.randint(1, 100))
