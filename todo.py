class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        """Adds a new task to the list."""
        self.tasks.append(task)
        #added task number to initial print after adding a task
        print(f'Task added: {task}   Task Number:', len(self.tasks))
        print(f'Task', len(self.tasks), 'added: {task}')

    def list_tasks(self):
        """Lists all tasks in the to-do list, including due dates if available."""
        if not self.tasks:
            print("No tasks in the list!")
        else:
            print("\nCurrent To-Do List:")
            for idx, task in enumerate(self.tasks, start=1):
                if isinstance(task, tuple):  # Task with due date
                    task_name, due_date = task
                    print(f'{idx}. {task_name} (Due: {due_date})')
                else:  # Task without due date
                    print(f'{idx}. {task}')

    def add_task_date(self, task_number, due_date):
        """Adds or updates a due date for a specific task."""
        if task_number <= 0 or task_number > len(self.tasks):
            print("Invalid task number! Please enter a valid number.")
        else:
            task = self.tasks[task_number - 1]
            if isinstance(task, str):
                # Task has no due date, so add one
                self.tasks[task_number - 1] = (task, due_date)
            else:
                # Task already has a due date, so update it
                task_name, _ = task
                self.tasks[task_number - 1] = (task_name, due_date)
            
            print(f'Task updated: {self.tasks[task_number - 1]}')

    def delete_task(self, task_number):
        """Deletes a task by its number in the list."""
        if task_number <= 0 or task_number > len(self.tasks):
            print("Invalid task number! Please enter a valid number.")
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
    print("5. Quit")


def main():
    """Main function that runs the To-Do List CLI."""
    todo_list = TodoList()

    while True:
        print_menu()
        choice = input("\nEnter your choice (1-5): ")

        if choice == '1':
            task = input("Enter the task: ")
            todo_list.add_task(task)

        elif choice == '2':
            todo_list.list_tasks()

        elif choice == '3':
            try:
                todo_list.list_tasks()
                task_number = int(input("Enter task number to delete: "))
                todo_list.delete_task(task_number)
                
            except ValueError:
                print("Invalid input! Please enter a valid number.")

        elif choice == '4':
            try:
                todo_list.list_tasks()
                task_number = int(input("Enter task number to update: "))
                due_date = input("Enter a due date for the task: ")
                task_number = int(input("Enter task number to add/update a due date: "))
                due_date = input("Enter a due date for the task (e.g., YYYY-MM-DD): ")
                todo_list.add_task_date(task_number, due_date)
                
            except ValueError:
                print("Invalid input! Please enter a valid number.")

        elif choice == '5':
            print("Exiting To-Do List CLI App. Goodbye!")
            break

        else:
            print("Invalid choice! Please choose a valid option.")


if __name__ == '__main__':
    main()
