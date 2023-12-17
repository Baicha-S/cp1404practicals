"""
Project Management Program.
Estimate time: 1 hour
"""

from datetime import datetime
from project import Project

FILENAME = "projects.txt"
MENU = "-(L)oad Project\n" \
       "-(S)ave Project\n" \
       "-(D)isplay Project\n" \
       "-(F)ilter projects by dates\n" \
       "-(A)dd new project\n" \
       "-(U)pdate project"


def main():
    """Run the program."""
    print(MENU)
    projects = []
    choice = input(">>> ").upper()
    while choice != "":
        if choice == "L":
            load_project(projects)
        elif choice == "S":
            save_project()
        elif choice == "D":
            display_project(projects)
        elif choice == "F":
            filter_project()
        elif choice == "A":
            add_project()
        elif choice == "U":
            update_project()
        else:
            print("Invalid choice.")
        choice = input(">>> ").upper()
    print("Thank you for using custom-built project management software.")


def load_project(projects):
    """Read the file."""
    filename_to_load = input("Project filename: ")
    with open(filename_to_load, 'r') as in_file:
        in_file.readline()
        for line in in_file:
            parts = line.strip().split("\t")
            project = Project(parts[0], parts[1], parts[2], float(parts[3]), int(parts[4]))
            projects.append(project)


def display_project(projects):
    """Display projects according to completion."""
    # for project in projects:
    #     print(project.completion_percentage)
    print("Incomplete projects: ")
    for project in projects:  # loop 1 for incomplete project.
        if project.completion_percentage != 100:
            print(project)

    print("Completed projects: ")
    for project in projects:  # loop 2 for completed project.
        if project.completion_percentage == 100:
            print(project)


def save_project():
    filename_to_save = input("")


def filter_project():
    pass


def add_project():
    pass


def update_project():
    pass


main()
