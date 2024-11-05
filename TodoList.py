class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task, date):
        """Adds a new task to the list."""
        if not self.tasks:
            print("No tasks in the list! Please start by listing tasks.")
            return
        
        task = (task, date)
        self.tasks.append(task)
        print(f'Task added: {task}')

    def list_tasks(self):
        """Lists all tasks in the to-do list."""
        if not self.tasks:
            print("No tasks in the list!")
        else:
            for idx, task in enumerate(self.tasks, start=1):
                print(f'{idx}. {task}')

    
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

    def delete_task(self, task_number):
        """Deletes a task by its number in the list."""
        if not self.tasks:
            print("No tasks in the list to delete!")
            return

        if task_number <= 0 or task_number > len(self.tasks):
            print("Invalid task number!")
        else:
            removed_task = self.tasks.pop(task_number - 1)
            print(f'Task removed: {removed_task}')

    def update_task(self, task_number, updated_message):
        """Change the description of a task"""
        if not self.tasks:
            print("No tasks in the list to update!")
            return

        if task_number <= 0 or task_number > len(self.tasks):
            print("Invalid task number!")
        else:
            task = self.tasks[task_number - 1]
            if type(task) is str:
                self.tasks[task_number - 1] = updated_message
            else:
                due_date = task[1]
                self.tasks[task_number - 1] = (updated_message, due_date)
            print("Task updated successfully!")

    def delete_all_tasks(self):
        """Deletes all tasks in the list."""
        if not self.tasks:
            print("No tasks to delete.")
        else:
            self.tasks = []
            print("All tasks deleted.")
