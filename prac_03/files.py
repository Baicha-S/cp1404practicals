# 1
name = input("Name: ")
out_file = open("name.txt", 'w')
print(name, file=out_file)
out_file.close()

# 2
in_file = open("name.txt", 'r')
name = in_file.read()
in_file.close()
print(f"Your name is {name}")

# 3
NUMBER_OF_LINE = 2
in_file = open("numbers.txt", 'r')
total = 0
for line in range(NUMBER_OF_LINE):
    number = int(in_file.readline())
    total += number
in_file.close()
print(total)

# 4
in_file = open("numbers.txt", 'r')
count = 0
lines = in_file.readlines()
for line in lines:
    count += 1
print(f"{count} lines")
