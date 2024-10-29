# todo.py
from TodoList import TodoList 

class TodoList:
    def __init__(self):
        self.tasks = []


  #this method was generated by ChatGPT as well as the subsequent adjustments
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


    def delete_task(self, task_number):
        """Deletes a task by its number in the list."""
        if task_number <= 0 or task_number > len(self.tasks):
            print("Invalid task number!")


    #that were made to print_menu and main
    def get_total_tasks(self):
        """Returns the total number of tasks in the to-do list."""
        return len(self.tasks)
   
    def add_task(self, task, priority = "Medium", date = None):
        """Adds a new task to the list if it doesn't already exist."""

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

        return None  # Task does not exist



    def list_tasks(self):
        """Lists all tasks in the to-do list, including due dates and priorities."""

    def list_tasks_numeric(self):
        """Lists all tasks in the to-do list in numerical order, including due dates if available."""

        if not self.tasks:
            print("No tasks in the list!")
        else:
            print("\nCurrent To-Do List:")
            for idx, task in enumerate(self.tasks, start=1):
                task_name, due_date, priority = task
                if due_date:
                    print(f'{idx}. {task_name} (Due: {due_date}) [Priority: {priority}]')
                else:
                    print(f'{idx}. {task_name} [Priority: {priority}]')

    #Good job with implementing this function and listing the list in alphabetical order
    def list_tasks_alphabetic(self):
        """ists all tasks in the to-do list in alphabetical order, including due dates if available."""
        if not self.tasks:
            print("No tasks in the list!")
        else:
            sorted_tasks = [] 
            #Although I would review the for loops to make code smaller and faster
            for idx, task in enumerate(self.tasks, start=1):
                item = (idx, task) 
                sorted_tasks.append(item)
            sorted_tasks = sorted(sorted_tasks, key=lambda x: x[1][0].lower() if isinstance(x[1], tuple) else x[1].lower())
            for idx, task in sorted_tasks:
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
            task_name, _, priority = self.tasks[task_number - 1]
            self.tasks[task_number - 1] = (task_name, due_date, priority)
            print(f'Task updated with due date: {self.tasks[task_number - 1]}')

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

    def update_task(self, task_number, updated_message):
        """Change the description of a task."""
        if task_number <= 0 or task_number > len(self.tasks):
            print("Invalid task number!")
        else:

            task_name, due_date, priority = self.tasks[task_number - 1]
            self.tasks[task_number - 1] = (updated_message, due_date, priority)
            print(f'Task updated: {self.tasks[task_number - 1]}')


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
            

 
    
    def change_task(self, task_number,new_task):
        #checking if task actually exists
        return

    def remove_due_date(self, task_number):
        """Removes the due date from a task."""

        if task_number <= 0 or task_number > len(self.tasks):
            print("Invalid task number!")
        else:
            task = self.tasks[task_number - 1]


            if type(task) is str:
                self.tasks[task_number - 1] = (new_task)
            else:
                task_name = task[0]
                self.tasks[task_number - 1] = (new_task)
            
            print(f'Task updated: {self.tasks[task_number - 1]}')


            if type(task) is tuple:  # Check if the task has a due date (stored as a tuple)
               task_name = task[0]
               self.tasks[task_number - 1] = task_name  # Remove due date by converting it back to a string
               print(f'Due date removed from task: {task_name}')
            else:
                print("This task doesn't have a due date.")



            
    def delete_all_tasks(self):
        self.tasks = []
        print("All tasks deleted.")
        
        # Overloading is not supported in python, this method overwrites previous
    # def add_task(self, task):
    #     """Adds a new task to the list."""
    #     self.tasks.append(task)
    #     print(f'Task added: {task}')

    def list_tasks(self):
        #Lists all tasks in the to-do list.
        if not self.tasks:
            print("No tasks in the list!")
        else:
            for idx, task in enumerate(self.tasks, start=1):
                print(f'{idx}. {task}')

    def add_task_date(self, task_number, due_date):
        """Add a due date to a task."""
        if not self.tasks:
            print("No tasks in the list to update!")
            return
        
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
        if not self.tasks:
            print("No tasks in the list to add a tag!")
            return
        
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

def get_validated_task_number(todo_list):
    #Helper function to validate and return a task number from the user.
    try:
        task_number = int(input("Enter task number: "))
        if task_number <= 0 or task_number > todo_list.get_total_tasks():
            print("Invalid task number! Please enter a valid number.")
            return None
        return task_number
    except ValueError:
        print("Invalid input! Please enter a number.")
        return None

def get_user_choice():
    #Helper function to get and validate user's menu choice.
    try:
        choice = int(input("\nEnter your choice (1-14): "))
        return choice
    except ValueError:
        print("Invalid input! Please enter a number.")
        return None
#This is my menu
def print_menu():
    #Prints the menu of options for the user.
    print("\nTo-Do List CLI App")
    print("1. Add task")
    print("2. List tasks ordered numerically")
    print("3. List tasks ordered alphabetically")
    print("4. Delete task")
    print("5. Add/Update a due date to a task")
    print("6. Add/Update a tag to a task")
    print("7. Delete all tasks")
    print("8. Edit task description")
    print("9. Show total number of tasks")
    print("10. Delete a due date to a task")
    print("11. Delegate task to someone else")
    print("12. Change task name")
    print("13. Mark Task Complete")
    print("14. Quit")

def main():
    #Main function that runs the To-Do List CLI.
    todo_list = TodoList()

    while True:
        print_menu()
        choice = get_user_choice()
        if choice is None:
            continue  # Invalid input, prompt the menu again.

        if choice == 1:
            task = input("Enter the task: ").strip()
            date_choice = input("Would you like to add a due date? (1: Yes, 2: No): ").strip()
            due_date = input("Enter the due date: ") if date_choice == '1' else None
            priority = input("Enter the priority (Low/Medium/High): ").strip()
            todo_list.add_task(task, priority, due_date)

        elif choice == 2:
            todo_list.list_tasks_numeric()

        elif choice == 3:
            todo_list.list_tasks_alphabetic()

        elif choice == 4:
            task_number = get_validated_task_number(todo_list)
            if task_number:
                todo_list.delete_task(task_number)

        elif choice == 5:
            task_number = get_validated_task_number(todo_list)
            if task_number:
                due_date = input("Enter a due date for the task (e.g., YYYY-MM-DD): ")
                todo_list.add_task_date(task_number, due_date)

        elif choice == 6:
            task_number = get_validated_task_number(todo_list)
            if task_number:
                tag = input("Enter a tag for the task: ")
                todo_list.add_tag(task_number, tag)

        elif choice == 7:
            todo_list.delete_all_tasks()

        elif choice == 8:
            task_number = get_validated_task_number(todo_list)
            if task_number:
                desc = input("Enter new task description: ")
                todo_list.update_task(task_number, desc)

        elif choice == 9:
            total_tasks = todo_list.get_total_tasks()
            print(f'Total number of tasks: {total_tasks}')

        elif choice == 10:
            task_number = get_validated_task_number(todo_list)
            if task_number:
                todo_list.remove_due_date(task_number)

        elif choice == 11:
            task_number = get_validated_task_number(todo_list)
            if task_number:
                task_delegate = input("Enter the name of the delegate: ")
                todo_list.add_task_delegate(task_number, task_delegate)

        elif choice == 12:
            task_number = get_validated_task_number(todo_list)
            if task_number:
                new_task = input("Enter the new task name: ")
                todo_list.change_task(task_number, new_task)

        elif choice == 13:
            task_number = get_validated_task_number(todo_list)
            if task_number:
                todo_list.checkoff_task(task_number)

        elif choice == 14:
            print("Exiting To-Do List CLI App. Goodbye!")
            break

        else:
            print("Invalid choice! Please choose a valid option.")

if __name__ == '__main__':
    main()
