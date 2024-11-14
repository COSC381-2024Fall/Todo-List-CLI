from datetime import datetime

class TodoList:
    """A class to store and manage one list of tasks
    """
    def __init__(self):
        """initialize an empty list
        """
        self.tasks = []

        """Task is a 6-tuple (task, priority, date, tags, delegate, completed)
        """

    def add_task(self, task, priority = "Medium", date = None):
        """Adds a new task to the list if it doesn't already exist.

        Args:
            task (_type_): a string. Leading or trailing whitespace will be removed. Cannot add a duplicate task.
            priority (str, optional): the priority of the task. Defaults to "Medium".
            date (_type_, optional): the due date of the task. Defaults to None.
        """

        task = task.strip()  # Remove any leading/trailing whitespace
        task_number = self.task_exists(task)
        if task_number:
            print(f"Task '{task}' already exists at position {task_number}.")
            return

        self.tasks.append((task, priority, date, [], None, False))
        print(f"Task added: {task} with priority '{priority}' and due date: '{date}'")

    def list_tasks(self):
        """Lists all tasks in the to-do list.
        """
        if not self.tasks:
            print("No tasks in the list!")
        else:
            for idx, task in enumerate(self.tasks, start=1):
                print(f'{idx}. {task}')

    def list_tasks_numeric(self):
        """Lists all tasks in the to-do list in numerical order, including due dates if available.
        """
        if not self.tasks:
            print("No tasks in the list!")
        else:
            print("\nCurrent To-Do List:")
            for idx, task in enumerate(self.tasks, start=1):
                task_name, priority, due_date, _, _, _ = task
                if due_date:
                    print(f'{idx}. {task_name} (Due: {due_date}) [Priority: {priority}]')
                else:
                    print(f'{idx}. {task_name} (Due: None) [Priority: {priority}]')
                    
    # Good job with implementing this function and listing the list in alphabetical order
    def list_tasks_alphabetic(self):
        """lists all tasks in the to-do list in alphabetical order, 
           including due dates if available.
        """
        if not self.tasks:
            print("No tasks in the list!")
        else:
            sorted_tasks = [] 
            # Although I would review the for loops to make code smaller and faster
            for idx, task in enumerate(self.tasks, start=1):
                item = (idx, task) 
                sorted_tasks.append(item)
            sorted_tasks = sorted(sorted_tasks, key=lambda x: x[1][0].lower() if isinstance(x[1], tuple) else x[1].lower())
            for idx, task in sorted_tasks:
                if isinstance(task, tuple):  # Task with due date
                    task_name, priority, due_date, _, _, _ = task
                    if due_date:
                        print(f'{idx}. {task_name} (Due: {due_date}) [Priority: {priority}]')
                    else:
                        print(f'{idx}. {task_name} (Due: None) [Priority: {priority}]')
                else:  # Task without due date
                    # all the tasks should now be a tuple
                    raise Exception("Internal error: the task is not a tuple.")

    def delete_task(self, task_number):
        """Deletes a task by its number in the list.

        Args:
            task_number (_type_): an integer
        """
        if not self.tasks:
            print("No tasks in the list to delete!")
            return

        if task_number <= 0 or task_number > len(self.tasks):
            print("Invalid task number!")
        else:
            removed_task = self.tasks.pop(task_number - 1)
            print(f'Task removed: {removed_task}')


    # this method was generated by ChatGPT as well as the subsequent adjustments
    def add_task_date(self, task_number, due_date):
        """Adds or updates a due date for a specific task.

        Args:
            task_number (_type_): an integer
            due_date (_type_): string
        """
        if not self.tasks:
            print("No tasks in the list to update!")
            return
        
        if task_number <= 0 or task_number > len(self.tasks):
            print("Invalid task number!")
        else:
            try:
                # Validate date format
                datetime.strptime(due_date, "%Y-%m-%d")
            except ValueError:
                print("Invalid date format! Please enter the date in YYYY-MM-DD format.")
                return
        
            task_name, priority, _, tags, delegate, completed = self.tasks[task_number - 1]
            self.tasks[task_number - 1] = (task_name, priority, due_date, tags, delegate, completed)
            print(f'Task updated with due date: {self.tasks[task_number - 1]}')
            

    def add_tag(self, task_number, tag):
        if not self.tasks:
            print("No tasks in the list to add a tag!")
            return
        
        if task_number <= 0 or task_number > len(self.tasks):
            print("Invalid task number!")
        else:
            task = self.tasks[task_number - 1]
            if type(task) is tuple:
                task_name, priority, due_date, tags, delegate, _ = task
                tags.append(tag)
                print(f'Task updated: {self.tasks[task_number - 1]}')
            else:
                # all the tasks should now be a tuple
                raise Exception("Internal error: the task is not a tuple.")

    
    def update_task(self, task_number, updated_message):
        """Change the description of a task"""
        if not self.tasks:
            print("No tasks in the list to update!")
            return

        if task_number <= 0 or task_number > len(self.tasks):
            print("Invalid task number!")
        else:
            task_name, priority, due_date, tags, delegate, completed = self.tasks[task_number - 1]
            self.tasks[task_number - 1] = (updated_message, priority, due_date, tags, delegate, completed)
            print(f'Task updated: {self.tasks[task_number - 1]}')
            

    def delete_all_tasks(self):
        """Deletes all tasks in the list."""
        if not self.tasks:
            print("No tasks to delete.")
        else:
            self.tasks = []
            print("All tasks deleted.")

    # that were made to print_menu and main
    def get_total_tasks(self):
        """Returns the total number of tasks in the to-do list."""
        return len(self.tasks)

    def remove_due_date(self, task_number):
        """Removes the due date from a task."""

        if task_number <= 0 or task_number > len(self.tasks):
            print("Invalid task number!")
        else:
            task_name, priority, due_date, tags, delegate, completed = self.tasks[task_number - 1]
            if due_date is not None:  # Check if the task has a due date
                # Remove due date by converting it back to a string
                self.tasks[task_number - 1] = (task_name, priority, None, tags, delegate, completed)
                print(f'Due date removed from task: {task_name}')
            else:
                print("This task doesn't have a due date.")                

    def add_task_delegate(self, task_number, task_delegate):
        """Delegates a task to someone else."""
        if task_number <= 0 or task_number > len(self.tasks):
            print("Invalid task number!")
            return

        if not task_delegate.isalnum() or not task_delegate:
            print("Invalid delegate")
            return

        else:
            task_name, priority, due_date, tags, delegate, completed = self.tasks[task_number - 1]
            self.tasks[task_number - 1] = (task_name, priority, due_date, tags, task_delegate, completed)
            print(f"Task delegated to {task_delegate}: {self.tasks[task_number - 1]}")
        

    def task_exists(self, task):
        """Checks if a task already exists. Returns the task number if it exists, or None otherwise.

        Args:
            task (_type_): a string

        Returns:
            _type_: None if task does not exist. Int if task exists.
        """
        task = task.strip()

        for idx, t in enumerate(self.tasks):
            task_name = t[0].strip().lower()
            if task_name == task.lower():
                return idx + 1

        return None  # Task does not exist

    def checkoff_task(self,task_number):
        """Mark the task completed"""
        # Check if the provided task number is valid
        if task_number <= 0 or task_number > len(self.tasks): 
            print("Invalid task number!")
        else:
            task_name, priority, due_date, tags, delegate, completed = self.tasks[task_number - 1]
            self.tasks[task_number - 1] = (task_name, priority, due_date, tags, delegate, True)
            print(f'Task updated: {self.tasks[task_number - 1]}')
