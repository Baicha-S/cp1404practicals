"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""

LOWER_THRESHOLD = 0.1
UPPER_THRESHOLD = 0.15

sales = float(input("Enter sales: $"))
while sales >= 0:
    if sales < 1000:
        user_bonus = sales * LOWER_THRESHOLD
        print(f"User's bonus is {int(user_bonus)}")
    else:
        user_bonus = sales * UPPER_THRESHOLD
        print(f"User's bonus is {int(user_bonus)}")
    sales = float(input("Enter sales: $"))
