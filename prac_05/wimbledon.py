"""Wimbledon Gentlemen singles champion program."""

FILENAME = "wimbledon.cvs"
COUNTRY_INDEX = 1
CHAMPION_INDEX = 2


def main():
    """Display Wimbledon Champion details."""
    records = get_record()
    champion_to_count, countries = manipulate_record(records)
    display_results(champion_to_count, countries)


def manipulate_record(records):
    """Create a set of countries and a dictionary of champions."""
    champion_to_count = {}
    countries = set()  # use set to avoid repeated elements
    for record in records:
        countries.add(record[COUNTRY_INDEX])
        try:
            champion_to_count[record[CHAMPION_INDEX]] += 1
        except KeyError:
            champion_to_count[record[CHAMPION_INDEX]] = 1
        return champion_to_count, countries


def get_record():
    """Get the record from cvs file and store in the list."""
    records = []
    with open(FILENAME, "r", encoding="utf-8-sig") as in_file:
        in_file.readline()
        for line in in_file:
            parts = line.strip().split(",")
            records.append(parts)
    return records


def display_results(champion_to_count, countries):
    """Count total of champions, display champions and countries"""
    print("Wimbledon Champions: ")
    for name, count in champion_to_count.items():
        print(name, count)
    print()

    print(f"These {len(countries)} countries have won Wimbledon")
    print(", ".join(country for country in sorted(countries)))


main()
