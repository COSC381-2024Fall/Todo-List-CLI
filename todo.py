class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task, priority, date=None):
        """Adds a new task with a priority level to the list."""
        task = task.strip()  # Remove any leading/trailing whitespace
        task_number = self.task_exists(task)
        if task_number:
            print(f"Task '{task}' already exists at position {task_number}.")
            return

        if date is None:
            self.tasks.append((task, priority))
        else:
            self.tasks.append((task, priority, date))

        print(f"Task added: {task} with priority '{priority}'")

    def task_exists(self, task):
        """Checks if a task already exists. Returns the task number if it exists, or None otherwise."""
        task = task.strip()

        for idx, t in enumerate(self.tasks):
            task_name = t[0].strip().lower()
            if task_name == task.lower():
                return idx + 1

        return None

    def list_tasks(self):
        """Lists all tasks in the to-do list."""
        if not self.tasks:
            print("No tasks in the list!")
        else:
            print("\nCurrent To-Do List:")
            for idx, task in enumerate(self.tasks, start=1):
                task_name, priority = task[0], task[1]
                due_date = task[2] if len(task) > 2 else None
                if due_date:
                    print(f"{idx}. {task_name} (Due: {due_date}) [Priority: {priority}]")
                else:
                    print(f"{idx}. {task_name} [Priority: {priority}]")

    def delete_task(self, task_number):
        """Deletes a task by its number."""
        if task_number <= 0 or task_number > len(self.tasks):
            print("Invalid task number!")
        else:
            removed_task = self.tasks.pop(task_number - 1)
            print(f"Task removed: {removed_task}")

    def add_task_date(self, task_number, due_date):
        """Adds or updates a due date for a specific task."""
        if task_number <= 0 or task_number > len(self.tasks):
            print("Invalid task number!")
        else:
            task_name, priority = self.tasks[task_number - 1][:2]
            self.tasks[task_number - 1] = (task_name, priority, due_date)
            print(f"Task updated with due date: {self.tasks[task_number - 1]}")

    def update_task(self, task_number, updated_message):
        """Change the description of a task."""
        if task_number <= 0 or task_number > len(self.tasks):
            print("Invalid task number!")
        else:
            task_name, priority = self.tasks[task_number - 1][:2]
            self.tasks[task_number - 1] = (updated_message, priority)
            print(f"Task updated: {self.tasks[task_number - 1]}")

    def delete_all_tasks(self):
        """Deletes all tasks."""
        self.tasks = []
        print("All tasks deleted.")

    def remove_due_date(self, task_number):
        """Removes the due date from a task."""
        if task_number <= 0 or task_number > len(self.tasks):
            print("Invalid task number!")
        else:
            task_name, priority = self.tasks[task_number - 1][:2]
            self.tasks[task_number - 1] = (task_name, priority)
            print(f"Due date removed from task: {task_name}")

    def get_total_tasks(self):
        """Returns the total number of tasks."""
        return len(self.tasks)

def print_menu():
    """Prints the menu of options for the user."""
    print("\nTo-Do List CLI App")
    print("1. Add task")
    print("2. List tasks")
    print("3. Delete task")
    print("4. Add/Update a due date to a task")
    print("5. Update task description")
    print("6. Remove due date")
    print("7. Show total number of tasks")
    print("8. Delete all tasks")
    print("9. Quit")

def main():
    """Main function that runs the To-Do List CLI."""
    todo_list = TodoList()

    while True:
        print_menu()
        choice = input("\nEnter your choice (1-9): ")

        try:
            if choice == '1':
                task = input("Enter the task: ")
                priority = input("Enter priority (low, medium, high): ")
                todo_list.add_task(task, priority)

            elif choice == '2':
                todo_list.list_tasks()

            elif choice == '3':
                task_number = int(input("Enter task number to delete: "))
                todo_list.delete_task(task_number)

            elif choice == '4':
                task_number = int(input("Enter task number to add/update a due date: "))
                due_date = input("Enter the due date (YYYY-MM-DD): ")
                todo_list.add_task_date(task_number, due_date)

            elif choice == '5':
                task_number = int(input("Enter task number to update description: "))
                updated_message = input("Enter the updated task description: ")
                todo_list.update_task(task_number, updated_message)

            elif choice == '6':
                task_number = int(input("Enter task number to remove due date: "))
                todo_list.remove_due_date(task_number)

            elif choice == '7':
                print(f"Total number of tasks: {todo_list.get_total_tasks()}")

            elif choice == '8':
                todo_list.delete_all_tasks()

            elif choice == '9':
                print("Exiting To-Do List CLI App. Goodbye!")
                break

            else:
                print("Invalid choice! Please choose a valid option.")

        except ValueError:
            print("Invalid input! Please enter a valid number.")

if __name__ == '__main__':
    main()
