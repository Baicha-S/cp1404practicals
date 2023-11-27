"""
1 Write code that asks the user for their name,
then opens a file called "name.txt" and writes that name to it.
Remember to close your file.
"""
FILENAME = "name.txt"
name = input("Name: ")
out_file = open(FILENAME, 'w')
print(name, file=out_file)
out_file.close()

"""
2. In the same file, but as if it were a separate program) Write code that opens 
"name.txt" and reads the name (as above) then prints,
"Your name is Bob" (or whatever the name is in the file).
"""
in_file = open(FILENAME, 'r')
name = in_file.read()
print(f"Your name is {name}")
in_file.close()

# 3
FILENAME = "numbers.txt"
NUMBER_OF_LINE = 2
in_file = open(FILENAME, 'r')
total = 0
for line in range(NUMBER_OF_LINE):
    number = int(in_file.readline())
    total += number
print(total)
in_file.close()

# 4
FILENAME = "numbers.txt"
count = 0
in_file = open("numbers.txt", 'r')
lines = in_file.readlines()
for line in lines:
    count += 1
print(f"{count} lines")
in_file.close()
