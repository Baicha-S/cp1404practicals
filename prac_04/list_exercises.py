PROMPT_INPUT = 5
numbers = []
total = 0
for i in range(0, PROMPT_INPUT):
    number = int(input("Number: "))
    numbers.append(number)
    total += number
print(f"The first number is {numbers[0]}")
print(f"The last number is {numbers[-1]}")
print(f"The smallest number is {min(numbers)}")
print(f"The largest number is {max(numbers)}")
print(f"The average of the numbers is {total / len(numbers)}")
