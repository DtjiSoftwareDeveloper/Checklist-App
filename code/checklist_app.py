"""
This file contains code for the application "Checklist App".
Author: DtjiSoftwareDeveloper
"""


# Importing necessary library


import sys
import os
import copy
import pickle


# Creating static functions


def load_checklist(file_name):
    # type: (str) -> Checklist
    return pickle.load(open(file_name, "rb"))


def save_checklist(checklist, file_name):
    # type: (Checklist, str) -> None
    pickle.dump(checklist, open(file_name, "wb"))


def clear():
    # type: () -> None
    if sys.platform.startswith('win'):
        os.system('cls')  # For Windows System
    else:
        os.system('clear')  # For Linux System


# Creating necessary classes


class Task:
    """
    This class contains attributes of a task.
    """

    def __init__(self, description):
        # type: (str) -> None
        self.description: str = description
        self.status: str = "Not Started"

    def update_status(self, status):
        # type: (str) -> bool
        if status in ["Not Started", "In Progress", "Complete"]:
            self.status = status
            return True
        return False

    def __str__(self):
        # type: () -> str
        return str(self.description) + "\n" + "Status: " + str(self.status) + "\n"

    def clone(self):
        # type: () -> Task
        return copy.deepcopy(self)


class Checklist:
    """
    This class contains attributes of a list of tasks.
    """

    def __init__(self, tasks=None):
        # type: (list) -> None
        if tasks is None:
            tasks = []

        self.__tasks: list = tasks

    def __str__(self):
        # type: () -> str
        res: str = "Checklist contents:\n"  # initial value
        task_number: int = 1
        for task in self.__tasks:
            res += str(task_number) + ". " + str(task) + "\n"
            task_number += 1

        return res

    def get_tasks(self):
        # type: () -> list
        return self.__tasks

    def add_task(self, description):
        # type: (str) -> None
        self.__tasks.append(Task(description))

    def remove_task(self, task):
        # type: (Task) -> bool
        if task in self.__tasks:
            self.__tasks.remove(task)
            return True
        return False

    def clone(self):
        # type: () -> Checklist
        return copy.deepcopy(self)


# Creating main function to run the application.


def main():
    """
    This main function is used to run the application.
    :return: None
    """

    print("Welcome to 'Checklist App' by 'DtjiSoftwareDeveloper'.")
    print("This application is a checklist application to indicate the status of tasks.")

    # Automatically load saved task list
    file_name: str = "SAVED CHECKLIST"
    new_checklist: Checklist
    try:
        new_checklist = load_checklist(file_name)

        # Clearing up the command line window
        clear()

        print("Your checklist:\n" + str(new_checklist))

    except FileNotFoundError:
        new_checklist = Checklist()

    print("Enter 'Y' for yes.")
    print("Enter anything else for no.")
    continue_using: str = input("Do you want to continue using 'Checklist App'? ")
    while continue_using == "Y":
        # Asking the user what he/she wants to do
        allowed_actions: list = ["ADD TASK", "REMOVE TASK", "VIEW CHECKLIST", "UPDATE TASK STATUS"]
        print("Enter 'ADD TASK' to add a task.")
        print("Enter 'REMOVE TASK' to remove a task.")
        print("Enter 'VIEW CHECKLIST' to view your checklist.")
        print("Enter 'UPDATE TASK STATUS' to update the status of one of the tasks in the checklist.")
        action: str = input("What do you want to do? ")
        while action not in allowed_actions:
            print("Enter 'ADD TASK' to add a task.")
            print("Enter 'REMOVE TASK' to remove a task.")
            print("Enter 'VIEW CHECKLIST' to view your checklist.")
            print("Enter 'UPDATE TASK STATUS' to update the status of one of the tasks in the checklist.")
            action = input("Sorry, invalid input! What do you want to do? ")

        if action == "ADD TASK":
            clear()
            description: str = input("Please enter the description of the task you want to add: ")
            new_checklist.add_task(description)
        elif action == "REMOVE TASK":
            clear()
            print("Below is a list of tasks in your checklist: \n")
            for task in new_checklist.get_tasks():
                print(str(task) + "\n")

            task_index: int = int(input("Please enter the index of the task you want to remove (index 1 for the first "
                                        "task, index 2 for the next, and so on): "))
            while task_index < 1 or task_index > len(new_checklist.get_tasks()):
                task_index = int(
                    input("Sorry, invalid input! Please enter the index of the task you want to remove (index 1 for "
                          "the first task, index 2 for the next, and so on): "))

            to_be_removed: Task = new_checklist.get_tasks()[task_index - 1]
            new_checklist.remove_task(to_be_removed)
        elif action == "VIEW CHECKLIST":
            clear()
            print(new_checklist)
            print("\n")
            input_string: str = input("Enter anything to proceed: ")
        elif action == "UPDATE TASK STATUS":
            clear()
            print("Below is a list of tasks in your checklist: \n")
            for task in new_checklist.get_tasks():
                print(str(task) + "\n")

            task_index: int = int(input("Please enter the index of the task you want to update its status (index 1 "
                                        "for the first task, index 2 for the next, and so on): "))
            while task_index < 1 or task_index > len(new_checklist.get_tasks()):
                task_index = int(
                    input("Sorry, invalid input! Please enter the index of the task you want to update its status "
                          "(index 1 for the first task, index 2 for the next, and so on): "))

            to_be_updated: Task = new_checklist.get_tasks()[task_index - 1]
            new_status: str = input("Please enter 'Not Started', 'In Progress', or 'Complete'! ")
            while new_status not in ["Not Started", "In Progress", "Complete"]:
                new_status = input("Sorry, invalid input! Please enter 'Not Started', 'In Progress', or 'Complete'! ")

            to_be_updated.update_status(new_status)
        else:
            pass  # Do nothing

        clear()
        print("Enter 'Y' for yes.")
        print("Enter anything else for no.")
        continue_using = input("Do you want to continue using 'Checklist App'? ")
    # Automatically saving the checklist
    save_checklist(new_checklist, file_name)
    sys.exit()


if __name__ == '__main__':
    main()
