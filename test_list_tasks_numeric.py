import unittest
from TodoList import TodoList  # Adjust the import as needed for your project structure

class TestTodoListMethods(unittest.TestCase):
    
    def setUp(self):
        """Set up a fresh instance of TodoList for each test."""
        self.todo_list = TodoList()

    # Functional Requirement Tests
    def test_add_task_functional(self):
        """Test adding a task with valid inputs."""
        self.todo_list.add_task("Buy groceries", "High")
        self.assertEqual(len(self.todo_list.tasks), 1)
        self.assertEqual(self.todo_list.tasks[0][0], "Buy groceries")

    # Edge Case Tests
    def test_add_empty_task_name(self):
        """Test adding a task with an empty task name."""
        with self.assertRaises(ValueError):  # Assume you raise ValueError on invalid input
            self.todo_list.add_task("", "Medium")

    def test_add_task_with_none_priority(self):
        """Test adding a task with None as priority."""
        self.todo_list.add_task("Task with no priority")
        self.assertEqual(self.todo_list.tasks[0][1], "Medium")  # If Medium is the default

    def test_add_duplicate_task(self):
        """Test adding a duplicate task and expect it to reject or handle it."""
        self.todo_list.add_task("Buy groceries", "High")
        result = self.todo_list.add_task("Buy groceries", "Low")  # Adjust based on your method's behavior
        self.assertIsNone(result)  # If it rejects duplicates, check the expected behavior here.

    # Error Handling Tests
    def test_invalid_priority_level(self):
        """Test adding a task with an invalid priority level."""
        with self.assertRaises(ValueError):  # Expect an error if priority is invalid
            self.todo_list.add_task("Finish report", "Super High")

    def test_list_tasks_numeric_no_tasks(self):
        """Test listing tasks when no tasks are present."""
        tasks = self.todo_list.list_tasks_numeric()
        self.assertEqual(tasks, [])

    def test_list_tasks_numeric_with_tasks(self):
        """Test listing tasks in numeric order when tasks are present."""
        self.todo_list.add_task("Task 1", "Low")
        self.todo_list.add_task("Task 2", "Medium")
        tasks = self.todo_list.list_tasks_numeric()
        expected_output = [
            "1. Task 1 (Due: None) [Priority: Low]",
            "2. Task 2 (Due: None) [Priority: Medium]"
        ]
        self.assertEqual(tasks, expected_output)

if __name__ == '__main__':
    unittest.main()
