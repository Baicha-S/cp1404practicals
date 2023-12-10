"""
Programming language.py program
Starting time: 16:43
Finished time: 17:00
"""


class ProgrammingLanguage:
    def __init__(self, name, typing, reflection, year):
        """Initialize the ProgrammingLanguage instance."""
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def __str__(self):
        """Return programming language details."""
        return "{}, {} Typing, Reflection={}, First appeared in {}"\
            .format(self.name, self.typing, self.reflection, self.year)

    def is_dynamic(self):
        """Return dynamic string if language is dynamic."""
        return self.typing == "Dynamic"
