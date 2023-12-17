"""
Project Management Program.
Estimate time: 1 hour
"""

from project import Project
import datetime

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
            add_project()
        elif choice == "U":
            update_project()
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


def save_project(projects):
    """Write parts of the project to the file."""
    filename_to_save = input("Project filename to save: ")
    with open(filename_to_save, "a") as out_file:
        print("Name\tStart Date\tPriority\tCost Estimate\tCompletion Percentage", file=out_file)
        for project in projects:
            print(f"{project.name}\t {project.start_date}\t {project.priority}\t "
                  f"{project.cost_estimate}\t {project.completion_percentage}", file=out_file)


def filter_project(projects):
    date_string = input("Show projects that start after date (dd/mm/yy):")  # e.g., "30/9/2022"
    date = datetime.datetime.strptime(date_string, "%d/%m/%Y").date()

    projects.sort()
    for project in projects:
        print(project)

    # print(f"That day is/was {date.strftime('%A')}")
    # print(date.strftime("%d/%m/%Y"))


def add_project():
    pass


def update_project():
    pass


main()
