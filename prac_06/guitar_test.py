"""Guitar_test.py (testing)"""
from prac_06.guitar import Guitar


def run_test():
    """Run the test for the Guitar class."""
    name = "Gibson L-5 CES"
    year = 1923
    # cost = 16035.40

    guitar = Guitar(name, year)
    other = Guitar("Another Guitar", 2013)

    print("{} get_age() - Expected {}. Got {}".format(guitar.name, 100, guitar.get_age()))
    print("{} get_age() - Expected {}. Got {}".format(other.name, 10, other.get_age()))
    print("{} is_vintage() - Expected {}. Got {}".format(guitar.name, True, guitar.is_vintage()))
    print("{} is_vintage() - Expected {}. Got {}".format(other.name, False, other.is_vintage()))


run_test()
