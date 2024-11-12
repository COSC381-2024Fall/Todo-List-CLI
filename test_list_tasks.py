from TodoList import TodoList #Imports TodoList module
from pytest import fixture 

@fixture
def todo_list():
    """Create a fresh TodoList instance for each test."""
    return TodoList()

def test_empty_list(todo_list, capfd):
#Arrange
    todo_list.list_tasks()

#Act
    captured = capfd.readouterr()

#Assert
    assert "No tasks in the list!\n" in captured.out

def test_list_tasks_with_tasks(todo_list, capfd):
#Arrange
    todo_list.add_task("Task 1", priority="High", date="2024-01-01")
    todo_list.add_task("Task 2", priority="High", date="2024-01-01")
    todo_list.add_task("Task 3", priority="High", date="2024-02-01")
#Act
    todo_list.list_tasks()
    captured = capfd.readouterr()
#Assert
    assert "1. ('Task 1', 'High', '2024-01-01', [], None, False)" in captured.out
    assert "2. ('Task 2', 'High', '2024-01-01', [], None, False)" in captured.out
    assert "3. ('Task 3', 'High', '2024-02-01', [], None, False)" in captured.out

def test_list_tasks_with_no_dates(todo_list, capfd):
#Arrange
    todo_list.add_task("Task 1", priority="High",)
    todo_list.add_task("Task 2", priority="High",)
    todo_list.add_task("Task 3", priority="High",)
#Act
    todo_list.list_tasks()
    captured = capfd.readouterr()
#Assert
    assert "1. ('Task 1', 'High', None, [], None, False)" in captured.out
    assert "2. ('Task 2', 'High', None, [], None, False)" in captured.out
    assert "3. ('Task 3', 'High', None, [], None, False)" in captured.out

def test_list_1000_tasks(todo_list, capfd):
#Arrange
    for i in range(1, 1001):
        todo_list.add_task(f"Task {i}", priority="High")

#Act
    todo_list.list_tasks()
    captured = capfd.readouterr()
#Assert
    assert "1. ('Task 1', 'High', None, [], None, False)" in captured.out
    assert "500. ('Task 500', 'High', None, [], None, False)" in captured.out
    assert "1000. ('Task 1000', 'High', None, [], None, False)" in captured.out