# todo.py

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

    def add_task_delegate(self, task_number, task_delegate):
        """Delegates a task to someone else."""
        if task_number <= 0 or task_number > len(self.tasks):
            print("Invalid task number!")
        else:
            task = self.tasks[task_number - 1]
            if type(task) is str:
                task_name = task
                self.tasks[task_number - 1] = (task, None, task_delegate)
            else:
                task_name = task[0]
            if len(task) == 2:
                self.tasks[task_number - 1] = (task, task_delegate)
            else:
                self.tasks[task_number - 1] = (task_name, task_delegate)

        print(f"Task delegated to {task_delegate}: {self.tasks[task_number - 1]}")

    def delete_task(self, task_number):
        """Deletes a task by its number in the list."""
        if task_number <= 0 or task_number > len(self.tasks):
            print("Invalid task number!")
        else:
            removed_task = self.tasks.pop(task_number - 1)
            print(f'Task removed: {removed_task}')


def print_menu():
    print("\nTo-Do List CLI App")
    print("1. Add task")
    print("2. List tasks")
    print("3. Delete task")
    print("4. Add/Update a due date to a task")
    print("5. Delegate task to someone else")
    print("6. Quit")


def main():
    todo_list = TodoList()

    while True:
        print_menu()
        choice = input("\nEnter your choice (1-6): ")

        if choice == '1':
            task = input("Enter the task: ")
            todo_list.add_task(task)

        elif choice == '2':
            todo_list.list_tasks()

        elif choice == '3':
            try:
                task_number = int(input("Enter task number to delete: "))
                todo_list.delete_task(task_number)
            except ValueError:
                print("Invalid input! Please enter a number.")

        elif choice == '4':
            try:
                task_number = int(input("Enter task number to update: "))
                due_date = input("Enter a due date for the task: ")
                todo_list.add_task_date(task_number, due_date)
            except ValueError:
                print("Invalid input! Please enter a number.")

        elif choice == "5":
            try:
                task_number = int(input("Enter task number to delegate: "))
                task_delegate = input("Enter the name of the delegate: ")
                todo_list.add_task_delegate(task_number, task_delegate)
            except ValueError:
                print("Invalid input! Please enter a number.")    
        
        elif choice == '6':
            print("Exiting To-Do List CLI App. Goodbye!")
            break

        else:
            print("Invalid choice! Please choose a valid option.")


if __name__ == '__main__':
    main()
