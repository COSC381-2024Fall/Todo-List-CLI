import pytest
from pytest import fixture
from todo import TodoList

class EdgeTestingClass:

    @staticmethod
    def test_function_one():
        """Test delegating the first task in the list."""
        # Arrange
        todo_list = TodoList()
        todo_list.add_task("Task 1", "Medium", "2024-11-30")
        todo_list.add_task("Task 2", "High", "2024-12-01")

        # Act
        todo_list.add_task_delegate(1, "Emerald")

        # Assert
        delegate = todo_list.tasks[0][4]
        assert delegate == "Emerald", "Delegate for the first task should be 'Emerald'."

    @staticmethod
    def test_function_two():
        """Test delegating the last task in the list."""
        # Arrange
        todo_list = TodoList()
        todo_list.add_task("Task 1", "Medium", "2024-11-30")
        todo_list.add_task("Task 2", "High", "2024-12-01")

        # Act
        todo_list.add_task_delegate(2, "Bob")

        # Assert
        delegate = todo_list.tasks[-1][4]
        assert delegate == "Bob", "Delegate for the last task should be 'Bob'."

    @staticmethod
    def test_function_three():
        """Test delegating a task with an unusually long name."""
        # Arrange
        long_task_name = "This is an unusually long task name that exceeds typical lengths for testing purposes"
        todo_list = TodoList()
        todo_list.add_task(long_task_name, "Low", "2024-11-29")

        # Act
        todo_list.add_task_delegate(1, "Charlie")

        # Assert
        delegate = todo_list.tasks[0][4]
        assert delegate == "Charlie", "Delegate for the task with a long name should be 'Charlie'."

class ErrorTestingClass:

    @staticmethod
    def test_function_one():
        """Test handling of invalid task number (out of range)."""
        # Arrange
        todo_list = TodoList()
        todo_list.add_task("Task 1", "High", "2024-12-31")

        # Act and Assert
        try:
            todo_list.add_task_delegate(2, "John Doe")  # Invalid task number
        except Exception as e:
            assert str(e) == "Invalid task number!"

    @staticmethod
    def test_function_two():
        """Test handling of delegation on an empty task list."""
        # Arrange
        todo_list = TodoList()

        # Act and Assert
        try:
            todo_list.add_task_delegate(1, "John Doe")  # No tasks in list
        except Exception as e:
            assert str(e) == "No tasks in the list to add a tag!"

    @staticmethod
    def test_function_three():
        """Test handling of non-integer task number."""
        # Arrange
        todo_list = TodoList()
        todo_list.add_task("Task 1", "Medium", "2024-11-30")

        # Act and Assert
        try:
            todo_list.add_task_delegate("One", "John Doe")  # Non-integer task number
        except TypeError:
            print("TypeError caught as expected")
        except Exception as e:
            assert False, f"Unexpected exception: {e}"  # Fail if a different exception is raised
        else:
            assert False, "Expected a TypeError, but no exception was raised."

class NormalTestingClass:

    @staticmethod
    def test_function_one():

        #Arrange
        list = TodoList()
        list.add_task("Do something", "Very Important", "06/12/2002")

        #Act
        list.add_task_delegate(1,"Cromwell")
        theDelegate = list.tasks[0][4]

        #Assert
        assert "Cromwell" == theDelegate
    
    @staticmethod
    def test_function_two():
        

        #Arrange
        list = TodoList()
        list.add_task("Do something else", "Not Important", "2014-10-03")

        #Act
        list.add_task_delegate(1,"Emerald")
        theDelegate = list.tasks[0][4]

        #Assert
        assert "Emerald" == theDelegate
    
    @staticmethod
    def test_function_three():
        

        #Arrange
        list = TodoList()
        list.add_task("Don't do anything", "No worries", "2024-10-26")

        #Act
        list.add_task_delegate(1,"Zhang")
        theDelegate = list.tasks[0][4]

        #Assert
        assert "Zhang" == theDelegate


test = NormalTestingClass()
test_2 = ErrorTestingClass()
test_3 = EdgeTestingClass()


test.test_function_one()
test.test_function_two()
test.test_function_three()


test_2.test_function_one()
test_2.test_function_two()
test_2.test_function_three()

test_3.test_function_one()
test_3.test_function_two()
test_3.test_function_three()