from TodoList import TodoList  # Import TodoList class from the main module
from pytest import fixture

@fixture
def todo_list():
    """Create a fresh TodoList instance for each test."""
    return TodoList()

def test_empty_list(todo_list, capfd):
    """Test list_tasks on an empty to-do list."""
    todo_list.list_tasks()
    captured = capfd.readouterr()
    assert "No tasks in the list!" in captured.out

def test_list_tasks_with_dates(todo_list, capfd):
    """Test list_tasks with tasks that have due dates."""
    todo_list.add_task("Task 1", priority="High", date="2024-01-01")
    todo_list.add_task("Task 2", priority="Medium", date="2024-02-01")
    todo_list.list_tasks()
    captured = capfd.readouterr()
    assert "1. ('Task 1', 'High', '2024-01-01', [], None, False)" in captured.out
    assert "2. ('Task 2', 'Medium', '2024-02-01', [], None, False)" in captured.out

def test_list_tasks_without_dates(todo_list, capfd):
    """Test list_tasks with tasks that do not have due dates."""
    todo_list.add_task("Task 1", priority="Low")
    todo_list.add_task("Task 2", priority="Medium")
    todo_list.list_tasks()
    captured = capfd.readouterr()
    assert "1. ('Task 1', 'Low', None, [], None, False)" in captured.out
    assert "2. ('Task 2', 'Medium', None, [], None, False)" in captured.out

def test_list_1000_tasks(todo_list, capfd):
    """Test list_tasks with a large number of tasks to verify scalability."""
    for i in range(1, 1001):
        todo_list.add_task(f"Task {i}", priority="High")
    todo_list.list_tasks()
    captured = capfd.readouterr()
    assert "1. ('Task 1', 'High', None, [], None, False)" in captured.out
    assert "500. ('Task 500', 'High', None, [], None, False)" in captured.out
    assert "1000. ('Task 1000', 'High', None, [], None, False)" in captured.out
