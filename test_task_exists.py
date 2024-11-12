from todo import TodoList
from pytest import fixture

@fixture
def empty_todolist():
    return TodoList()

@fixture
def populated_todolist():
    todo_list = TodoList()
    todo_list.tasks = [
        ("Buy grocery", "Medium", "2024-12-02", [], "Long", False),
        ("Call doctor", "High", "2024-11-12", [], "Long", False),
        ("Finish homework", "High", None, ["school"], "Long", False)
    ]
    return todo_list

def test_task_exists_found(populated_todolist):
    """Check if an existing task is found by task_exists."""
    assert populated_todolist.task_exists("Buy grocery") == 1

def test_task_exists_not_found(populated_todolist):
    """Ensure task_exists returns None if the task is not in the list."""
    assert populated_todolist.task_exists("Go to gym") is None

def test_task_exists_case_insensitivity(populated_todolist):
    """Verify that task_exists is case-insensitive."""
    assert populated_todolist.task_exists("buy GROCERY") == 1

def test_task_exists_whitespace_handling(populated_todolist):
    """Check if task_exists handles leading and trailing whitespace correctly."""
    assert populated_todolist.task_exists("  Call doctor  ") == 2

def test_task_exists_empty_list(empty_todolist):
    """Test task_exists with an empty task list, expecting None."""
    assert empty_todolist.task_exists("Read book") is None

def test_task_exists_empty_string(populated_todolist):
    """Verify that an empty string as a task name returns None."""
    assert populated_todolist.task_exists("") is None

def test_task_exists_task_with_only_whitespace(populated_todolist):
    """Ensure task_exists returns None when searching for a name consisting only of whitespace."""
    assert populated_todolist.task_exists("   ") is None

def test_task_exists_multiple_same_name_tasks():
    """Check if task_exists returns the index of the first occurrence when duplicate task names are present."""
    todo_list = TodoList()
    todo_list.tasks = [
        ("Task A", "Medium", None, [], None, False),
        ("Task B", "High", "2024-11-10", [], "Long", False),
        ("Task B", "Low", None, ["personal"], "Long", False)
    ]
    assert todo_list.task_exists("Task B") == 2  # First occurrence should be returned