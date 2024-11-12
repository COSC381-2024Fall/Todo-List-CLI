import unittest
import sys
import os

sys.path.append(os.path.abspath('/home/ubuntu/mod21_TodoList_CTI/Todo-List-CLI'))
from TodoList import TodoList

class TestListTasksNumeric(unittest.TestCase):
    def test_list_tasks_numeric(self):
        # Initialize the TodoList object
        todo_list = TodoList()
        
        # Add tasks
        todo_list.add_task("Buy groceries", "Medium")
        todo_list.add_task("Walk the dog", "Medium")
        todo_list.add_task("Read a book", "Medium")
        
        # Get the list of tasks in numeric order
        tasks = todo_list.list_tasks_numeric()

        print(tasks) # print tasks to debug
        
        # Check if the tasks are listed in the expected format
        self.assertEqual(tasks, [
            "1. Buy groceries (Due: None) [Priority: Medium]",
            "2. Walk the dog (Due: None) [Priority: Medium]",
            "3. Read a book (Due: None) [Priority: Medium]"
        ])


if __name__ == '__main__':
    unittest.main()
