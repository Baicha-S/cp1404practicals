from prac_07.guitar import Guitar

FILENAME = "guitars.csv"

with open(FILENAME, 'r') as in_file:
    guitars = []
    in_file.readline()
    for line in in_file:
        parts = line.strip().split(',')

        guitar = Guitar(parts[0], parts[1], parts[2])
        guitars.append(guitar)

    # for guitar in guitars:
    #     print(guitar)

    guitars.sort()
    for guitar in guitars:
        print(guitar)

    name = input("Name: ")
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: $"))
        guitar = Guitar(name, year, cost)
        guitars.append(guitar)

        with open(FILENAME, 'a') as out_file:
            print(f"{name},{year},{cost}", file=out_file)

        name = input("Name: ")
