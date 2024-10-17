# todo.py

class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        """Adds a new task to the list if it doesn't already exist."""
        if self.task_exists(task):
            print(f"Task '{task}' already exists in the list! Cannot add duplicate tasks.")
        else:
            self.tasks.append(task)
            print(f'Task added: {task}')

    def task_exists(self, task):
        """Checks if a task already exists (case insensitive)."""
        for t in self.tasks:
            # Handling tuple case when task has a due date (e.g., (task_name, due_date))
            if (isinstance(t, tuple)):
                if t[0].lower() == task.lower():
                    return True
            else: 
                if t.lower() == task.lower():
                    return True
        return False 

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


    def update_task(self, task_number, updated_message):
        """Change the description of a task"""
        if task_number <= 0 or task_number > len(self.tasks):
            print("Invalid task number!")
        else:
            task = self.tasks[task_number - 1]
            if type(task) is str:
                self.tasks[task_number - 1] = updated_message
            else:
                due_date = task[1]
                self.tasks[task_number - 1] = (updated_message, due_date)


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
    print("5. Edit task description")
    print("6. Quit")


def main():
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
                task_number = int(input("Enter task number to delete: "))
                todo_list.delete_task(task_number)
            except ValueError:
                print("Invalid input! Please enter a number.")

        elif choice == '4':
            task_number = int(input("Enter task number to update: "))
            due_date = input("Enter a due date for the task: ")
            todo_list.add_task_date(task_number, due_date)

        elif choice == '5':
            try:
                task_number = int(input("Enter task number to update: "))
                desc = input("Enter new task description: ")
                todo_list.update_task(task_number, desc)
            except ValueError:
                print("Invalid input! Please enter a number.")    
        elif choice == '6':
            print("Exiting To-Do List CLI App. Goodbye!")
            break

        else:
            print("Invalid choice! Please choose a valid option.")


if __name__ == '__main__':
    main()
