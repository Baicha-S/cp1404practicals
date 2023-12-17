"""
Project Management Program.
Estimate time: 1 hour
"""

from project import Project
from datetime import datetime

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
            save_project(projects)
        elif choice == "D":
            display_project(projects)
        elif choice == "F":
            filter_project(projects)
        elif choice == "A":
            add_project(projects)
        elif choice == "U":
            update_project(projects)
        else:
            print("Invalid choice.")
        choice = input(">>> ").upper()
    print("Thank you for using custom-built project management software.")


def load_project(projects):
    """Read the file."""
    filename_to_load = input("Project filename to load: ")
    with open(filename_to_load, 'r') as in_file:
        in_file.readline()
        for line in in_file:
            parts = line.strip().split("\t")
            project = Project(parts[0], datetime.strptime(parts[1], "%d/%m/%Y").date(),
                              parts[2], float(parts[3]), int(parts[4]))
            projects.append(project)


def display_project(projects):
    """Display projects according to completion."""
    projects.sort()
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


def save_project(projects):
    """Write parts of the project to the file."""
    filename_to_save = input("Project filename to save: ")
    with open(filename_to_save, "a") as out_file:
        print("Name\tStart Date\tPriority\tCost Estimate\tCompletion Percentage", file=out_file)
        for project in projects:
            print(f"{project.name}\t {project.start_date}\t {project.priority}\t "
                  f"{project.cost_estimate}\t {project.completion_percentage}", file=out_file)


def filter_project(projects):
    """Filter the project according to input date."""
    start_date_string = input("Show projects that start after date (dd/mm/yy):")  # e.g., "30/9/2022"
    start_date = datetime.strptime(start_date_string, "%d/%m/%Y").date()

    for project in projects:
        if project.is_greater(start_date):
            print(project)

    print(f"That day is/was {start_date.strftime('%A')}")
    print(start_date.strftime("%d/%m/%Y"))


def add_project(projects):
    """Add new project to projects."""
    print("Let's add a new project")
    name = input("Name: ")
    start_date = input("Start date (dd/mm/yy):")
    priority = int(input("Priority:"))
    cost_estimate = float(input("Cost estimate: $"))
    completion_percentage = int(input("Percent complete: "))

    project = Project(name, datetime.strptime(start_date, "%d/%m/%Y").date(),
                      priority, cost_estimate, completion_percentage)
    projects.append(project)


def update_project(projects):
    """Update project data."""
    for index, project in enumerate(projects):  # loop first time to display index.
        print(index, project)

    project_choice = int(input("Project choice: "))  # input is index.
    print(projects[project_choice])

    for index, project in enumerate(projects):  # loop 2nd time to catch choice.
        if project_choice == index:
            new_percentage = int(input("New percentage: "))
            new_priority = input("Priority: ")

            project.completion_percentage = new_percentage
            project.priority = new_priority


main()
