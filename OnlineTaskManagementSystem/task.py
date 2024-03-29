# Description: Build an online task management system that allows users to create, view, update, and delete tasks. The system should provide features like task prioritization, due dates, status updates, and error handling for input validation.
"""
Pseudo Code:

1. Define a Task class with attributes: title, description, due date, priority, and status.

2. Implement error handling for input validation (e.g., ensuring the due date is a valid date, priority is within a valid range, etc.).

3. Create a TaskManager class to manage tasks:

o Initialize an empty list to store tasks. • Implement methods to add_task, update_task, delete_task, and view_tasks.

o Allow users to input task details and handle errors appropriately.

4. Utilize Object-Oriented Programming (OOP) concepts to encapsulate data and logic within classes and methods.

5. Develop a user interface for interaction, displaying options like create task, update task, view tasks, and delete task.
"""

# Importing the required modules
import datetime
import re

# Defining a Task class with attributes: title, description, due date, priority, and status.
class Task:
    def __init__(self, title, description, due_date, priority, status):
        self.title = title
        self.description = description
        self.due_date = due_date
        self.priority = priority
        self.status = status

# Implementing error handling for input validation (e.g., ensuring the due date is a valid date, priority is within a valid range, etc.).

    # Function to validate the due date
    def validate_due_date(self, due_date):
        try:
            datetime.datetime.strptime(due_date, '%Y-%m-%d')
            return True
        except ValueError:
            return False
        
    # Function to validate the priority
    def validate_priority(self, priority):
        if priority in range(1, 6):
            return True
        else:
            return False
        
    # Function to validate the status
    def validate_status(self, status):
        if status in ['Not Started', 'In Progress', 'Completed']:
            return True
        else:
            return False
        
# Creating a TaskManager class to manage tasks:
class TaskManager:

    # Initializing an empty list to store tasks.
    def __init__(self):
        self.tasks = []
        
    # Implementing methods to add_task, update_task, delete_task, and view_tasks.
    
    # Function to add a task
    def add_task(self, task):
        self.tasks.append(task)
        
    # Function to update a task
    def update_task(self, task):
        for i in range(len(self.tasks)):
            if self.tasks[i].title == task.title:
                self.tasks[i] = task
                break
                
    # Function to delete a task
    def delete_task(self, task):
        for i in range(len(self.tasks)):
            if self.tasks[i].title == task.title:
                del self.tasks[i]
                break
                
    # Function to view all the tasks
    def view_tasks(self):
        for task in self.tasks:
            print("Title: ", task.title)
            print("Description: ", task.description)
            print("Due Date: ", task.due_date)
            print("Priority: ", task.priority)
            print("Status: ", task.status)
            print("")

# Allowing users to input task details and handle errors appropriately.
def main():
    task_manager = TaskManager()
    while True:
        print("1. Create Task")
        print("2. Update Task")
        print("3. Delete Task")
        print("4. View Tasks")
        print("5. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            title = input("Enter the title of the task: ")
            description = input("Enter the description of the task: ")
            due_date = input("Enter the due date of the task (YYYY-MM-DD): ")
            while not Task.validate_due_date(Task, due_date):
                due_date = input("Enter the due date of the task (YYYY-MM-DD): ")
            priority = int(input("Enter the priority of the task (1-5): "))
            while not Task.validate_priority(Task, priority):
                priority = int(input("Enter the priority of the task (1-5): "))
            status = input("Enter the status of the task (Not Started, In Progress, Completed): ")
            while not Task.validate_status(Task, status):
                status = input("Enter the status of the task (Not Started, In Progress, Completed): ")
            task = Task(title, description, due_date, priority, status)
            task_manager.add_task(task)
        elif choice == "2":
            title = input("Enter the title of the task to be updated: ")
            description = input("Enter the description of the task: ")
            due_date = input("Enter the due date of the task (YYYY-MM-DD): ")
            while not Task.validate_due_date(Task, due_date):
                due_date = input("Enter the due date of the task (YYYY-MM-DD): ")
            priority = int(input("Enter the priority of the task (1-5): "))
            while not Task.validate_priority(Task, priority):
                priority = int(input("Enter the priority of the task (1-5): "))
            status = input("Enter the status of the task (Not Started, In Progress, Completed): ")
            while not Task.validate_status(Task, status):
                status = input("Enter the status of the task (Not Started, In Progress, Completed): ")
            task = Task(title, description, due_date, priority, status)
            task_manager.update_task(task)
        elif choice == "3":
            title = input("Enter the title of the task to be deleted: ")
            task = Task(title, None , None, None, None)
            task_manager.delete_task(task)
        elif choice == "4":
            task_manager.view_tasks()
        elif choice == "5":
            break
        else:
            print("Invalid Choice")

# Calling the main function
if __name__ == "__main__":
    main()

# Output:
"""
1. Create Task
2. Update Task
3. Delete Task
4. View Tasks
5. Exit
Enter your choice: 1
Enter the title of the task: Task 1
Enter the description of the task: This is task 1
Enter the due date of the task (YYYY-MM-DD): 2021-10-10
Enter the priority of the task (1-5): 1
Enter the status of the task (Not Started, In Progress, Completed): Not Started
1. Create Task
2. Update Task
3. Delete Task
4. View Tasks
5. Exit
Enter your choice: 1
Enter the title of the task: Task 2
Enter the description of the task: This is task 2
Enter the due date of the task (YYYY-MM-DD): 2021-10-11
Enter the priority of the task (1-5): 2
Enter the status of the task (Not Started, In Progress, Completed): In Progress
1. Create Task
2. Update Task
3. Delete Task
4. View Tasks
5. Exit
Enter your choice: 1
Enter the title of the task: Task 3
Enter the description of the task: This is task 3
Enter the due date of the task (YYYY-MM-DD): 2021-10-12
Enter the priority of the task (1-5): 3
Enter the status of the task (Not Started, In Progress, Completed): Completed
1. Create Task
2. Update Task
3. Delete Task
4. View Tasks
5. Exit
Enter your choice: 4
Title:  Task 1
Description:  This is task 1
Due Date:  2021-10-10
Priority:  1
Status:  Not Started

Title:  Task 2
Description:  This is task 2
Due Date:  2021-10-11
Priority:  2
Status:  In Progress

Title:  Task 3
Description:  This is task 3
Due Date:  2021-10-12
Priority:  3
Status:  Completed

1. Create Task
2. Update Task
3. Delete Task
4. View Tasks
5. Exit
Enter your choice: 2
Enter the title of the task to be updated: Task 2
Enter the description of the task: This is task 2
Enter the due date of the task (YYYY-MM-DD): 2021-10-13
Enter the priority of the task (1-5): 4
Enter the status of the task (Not Started, In Progress, Completed): Completed
1. Create Task
2. Update Task
3. Delete Task
4. View Tasks
5. Exit
Enter your choice: 4
Title:  Task 1
Description:  This is task 1
Due Date:  2021-10-10
Priority:  1
Status:  Not Started

Title:  Task 2
Description:  This is task 2
Due Date:  2021-10-13
Priority:  4
Status:  Completed

Title:  Task 3
Description:  This is task 3
Due Date:  2021-10-12
Priority:  3
Status:  Completed

1. Create Task
2. Update Task
3. Delete Task
4. View Tasks
5. Exit
Enter your choice: 3
Enter the title of the task to be deleted: Task 3
1. Create Task
2. Update Task
3. Delete Task
4. View Tasks
5. Exit
Enter your choice: 4
Title:  Task 1
Description:  This is task 1
Due Date:  2021-10-10
Priority:  1
Status:  Not Started

Title:  Task 2
Description:  This is task 2
Due Date:  2021-10-13
Priority:  4
Status:  Completed

1. Create Task
2. Update Task
3. Delete Task
4. View Tasks
5. Exit
Enter your choice: 5
"""
