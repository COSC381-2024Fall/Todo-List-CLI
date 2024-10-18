class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task, date = None):
        """Adds a new task to the list if it doesn't already exist."""
        task = task.strip()  # Remove any leading/trailing whitespace
        task_number = self.task_exists(task)
        if task_number:
            print(f"Task '{task}' already exists in the list at position {task_number}. Cannot add duplicate tasks.")
            return

        if date == None:
            self.tasks.append(task)
        else:
            self.tasks.append((task, date))
            
        print(f'Task added: {task}')

    def task_exists(self, task):
        """Checks if a task already exists (case insensitive, ignores trailing whitespace). 
        Returns the task number if it exists, or None otherwise."""
        task = task.strip()  # Ensure we ignore leading/trailing whitespace

        for idx, t in enumerate(self.tasks):
            # If task is a tuple, compare only the task name (ignores due date)
            if isinstance(t, tuple):
                task_name = t[0].strip().lower()
                if task_name == task.lower():
                    return idx + 1  # Return the 1-based index of the task
            else:
                if t.strip().lower() == task.lower():
                    return idx + 1  # Return the 1-based index of the task

        return None  # Task does not exist

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


    def update_task(self, task_number, updated_message):
        """Change the description of a task"""
        if task_number <= 0 or task_number > len(self.tasks):
            print("Invalid task number!")
        else:
            task_name = task[0]
            self.tasks[task_number - 1] = f"{due_date}: {task_name}" 
        
        print(f'Task updated: {self.tasks[task_number - 1]}')
        
    def delete_task(self, task_number):
        """Deletes a task by its number in the list."""
        if task_number <= 0 or task_number > len(self.tasks):
            print("Invalid task number! Please enter a valid number.")
        else:
            removed_task = self.tasks.pop(task_number - 1)
            print(f'Task removed: {removed_task}')
    
    def checkoff_task(self,task_number):
        """Mark the task completed"""
        # Check if the provided task number is valid
        if task_number <= 0 or task_number > len(self.tasks): 
            print("Invalid task number!")
        else:
            task = self.tasks[task_number - 1]
            if type(task) is str:
                self.tasks[task_number - 1] = (task, "completed") # Replace the task with a tuple (task name, "completed") to mark it as completed
            else:
                # If the task already has a due date, preserve the task name
                task_name = task[0]
                self.tasks[task_number - 1] = (task_name, "completed")
            


def print_menu():
    """Prints the menu of options for the user."""
    print("\nTo-Do List CLI App")
    print("1. Add task")
    print("2. List tasks")
    print("3. Delete task")
    print("4. Add/Update a due date to a task")
    print("5. Add/Update a tag to a task")
    print("6. Mark Task Completed")
    print("7. Delete All Tasks")
    print("8. Update/Modify Task")
    print("9. Quit")


def main():
    """Main function that runs the To-Do List CLI."""
    todo_list = TodoList()

    while True:

        print_menu()
        choice = input("\nEnter your choice (1-6): ")

        try: 
            print_menu()
            choice = input("\nEnter your choice (1-8): ")

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
                try:
                    todo_list.list_tasks()
                    task_number = int(input("Enter task number to delete: "))
                    todo_list.delete_task(task_number)
                    
                except ValueError:
                    print("Invalid input! Please enter a valid number.")

            elif choice == '4':
                task_number = int(input("Enter task number to add/update a due date: "))
                due_date = input("Enter a due date for the task (e.g., YYYY-MM-DD): ")
                todo_list.add_task_date(task_number, due_date)
                
        #   Add/Update a tag
            elif choice == '5':
                task_number = int(input("Enter task number to update: "))
                tag = input("Enter a tag for the task: ")
                todo_list.add_tag(task_number, tag)
            
        #   Mark Completed 
            elif choice == '6':
            try:
                task_number = int(input("Enter task number to Mark Completed: "))
                todo_list.checkoff_task(task_number)
            except ValueError:
                print("Invalid input! Please enter a number.")
            
            

            elif choice == '7':
                todo_list.delete_all_tasks()

            elif choice == '8':
                try:
                    task_number = int(input("Enter task number to update: "))
                    desc = input("Enter new task description: ")
                    todo_list.update_task(task_number, desc)
                except ValueError:
                    print("Invalid input! Please enter a number.")    

            elif choice == '9':
                print("Exiting To-Do List CLI App. Goodbye!")
                break
                
                
                
                
                


if __name__ == '__main__':
    main()