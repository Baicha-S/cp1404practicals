"""Guitar.py (the class)"""


CURRENT_YEAR = 2023
VINTAGE_THRESHOLD = 50


class Guitar:
    def __init__(self, name="", year=0, cost=0):
        """Initialize the Guitar instance."""

        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Return a string that show guitar information."""
        return "{} ({}) : ${}".format(self.name, self.year, self.cost)

    def get_age(self):
        """Return the age of guitar."""
        return CURRENT_YEAR - self.year

    def is_vintage(self):
        """Determine whether guitar is vintage or not."""
        return self.get_age() >= VINTAGE_THRESHOLD

    def __lt__(self, other):
        """Return data that is less than."""
        return self.year < other.year
