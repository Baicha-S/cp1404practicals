"""Project class program."""


class Project:
    """Project class."""
    def __init__(self, name, start_date, priority, cost_estimate, completion_percentage):
        """Initialize the project instance."""
        self.name = name
        self.start_date = start_date
        self.priority = priority
        self.cost_estimate = cost_estimate
        self.completion_percentage = completion_percentage

    def __str__(self):
        """Return data as a string."""
        return f"{self.name}, start: {self.start_date}, priority {self.priority}," \
               f"estimate: ${self.cost_estimate}, completion: {self.completion_percentage}%"

    def __lt__(self, other):
        """Return data that is less than."""
        return self.priority < other.priority

    def is_greater(self, start_date):
        """Determine whether input datetime is greater or not. """
        return self.start_date > start_date
