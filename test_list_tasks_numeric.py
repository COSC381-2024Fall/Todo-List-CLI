import unittest
from TodoList import TodoList

class TestListTasksNumeric(unittest.TestCase):
    def setUp(self):
        # Create a TodoList instance and add tasks for testing
        self.todo_list = TodoList()
        self.todo_list.add_task("Buy groceries")
        self.todo_list.add_task("Walk the dog")
        self.todo_list.add_task("Read a book")

    def test_list_tasks_numeric(self):
        # List tasks and check if they are in numerical order
        tasks = self.todo_list.list_tasks()
        self.assertEqual(tasks, ["1. Buy groceries", "2. Walk the dog", "3. Read a book"])

if __name__ == '__main__':
    unittest.main()
