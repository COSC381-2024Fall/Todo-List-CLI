from task_manager_ import TaskManager

import unittest

class TestCheckoffTask(unittest.TestCase):
    def setUp(self):
        self.task_manager = TaskManager()
        self.task_manager.tasks = [
            {'description': 'Task 1', 'completed': False},
            {'description': 'Task 2', 'completed': True}  # Pre-completed for testing
        ]

    def test_valid_task_completion(self):
        self.task_manager.checkoff_task(0)  # Valid and not completed
        self.assertTrue(self.task_manager.tasks[0]['completed'])

    def test_already_completed_task(self):
        self.task_manager.checkoff_task(1)  # Already completed
        # Add checks for the printed output if required

    def test_invalid_task_number(self):
        self.task_manager.checkoff_task(10)  # Invalid task number
        # Add checks for the error message if required

    def test_non_integer_task_number(self):
        with self.assertRaises(TypeError):
            self.task_manager.checkoff_task("not an integer")  # Non-integer input

if __name__ == '__main__':
    unittest.main()
