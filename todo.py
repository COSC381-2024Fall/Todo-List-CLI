class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        """Adds a new task to the list."""
        self.tasks.append(task)
        print(f'Task added: {task}')

    def list_tasks(self):
        """Lists all tasks in the to-do list."""
        if not self.tasks:
            print("No tasks in the list!")
        else:
            for idx, task in enumerate(self.tasks, start=1):
                print(f'{idx}. {task}')

    def add_task_date(self, task_number, due_date):
        """Add a due date to a task."""
        if task_number <= 0 or task_number > len(self.tasks):
            print("Invalid task number!")
        else:
            task = self.tasks[task_number - 1]
            if type(task) is str:
                self.tasks[task_number - 1] = (task, due_date)
            else:
                task_name = task[0]
                self.tasks[task_number - 1] = (task_name, due_date)
            
            print(f'Task updated: {self.tasks[task_number - 1]}')

    def add_tag(self, task_number, tag):
        if task_number <= 0 or task_number > len(self.tasks):
            print("Invalid task number!")
        else:
            task = self.tasks[task_number - 1]
            if type(task) is str:
                due_date = "No Date Assigned"
                self.tasks[task_number - 1] = (task, due_date, tag)
            else:
                due_date = self.tasks[task_number-1][1]
                task_name = task[0]
                self.tasks[task_number - 1] = (task_name, due_date, tag)

            print(f'Task updated: {self.tasks[task_number - 1]}')


    def delete_task(self, task_number):
        """Deletes a task by its number in the list."""
        if task_number <= 0 or task_number > len(self.tasks):
            print("Invalid task number!")
        else:
            removed_task = self.tasks.pop(task_number - 1)
            print(f'Task removed: {removed_task}')


def print_menu():
    """Prints the menu of options for the user."""
    print("\nTo-Do List CLI App")
    print("1. Add task")
    print("2. List tasks")
    print("3. Delete task")
    print("4. Add/Update a due date to a task")
    print("5. Add/Update a tag to a task")
    print("6. Delete all tasks")
    print("7. Quit")


def main():
    """Main function that runs the To-Do List CLI."""
    todo_list = TodoList()

    while True:
        try:
            print_menu()
            choice = input("\nEnter your choice (1-6): ")

            if choice == '1':
                    task = input("Enter the task: ")
                    dateBool = input("Would you like to add a due date? 1: Yes 2: No -- ")
                    if int(dateBool) == 1:
                        due_date = input("Enter the due date: ")
                    else:
                        due_date = ""
                    todo_list.add_task(task, due_date)

            elif choice == '2':
                    todo_list.list_tasks()

            elif choice == '3':
                    task_number = int(input("Enter task number to delete: "))
                    todo_list.delete_task(task_number)

            elif choice == '4':
                    task_number = int(input("Enter task number to update: "))
                    due_date = input("Enter a due date for the task: ")
                    task_number = int(input("Enter task number to add/update a due date: "))
                    due_date = input("Enter a due date for the task (e.g., YYYY-MM-DD): ")
                    todo_list.add_task_date(task_number, due_date)
                    
            #   Add/Update a tag
            elif choice == '5':
                task_number = int(input("Enter task number to update: "))
                tag = input("Enter a tag for the task: ")
                todo_list.add_tag(task_number, tag)


            elif choice == '6':
                todo_list.delete_all_tasks()

            elif choice == '7':
                print("Exiting To-Do List CLI App. Goodbye!")
                break

            else:
                print("Invalid choice! Please choose a valid option.")
        except ValueError:
            print("Invalid input! Please enter a number.")


if __name__ == '__main__':
    main()
