import pytest
from pytest import fixture
from todo import TodoList

@fixture
def grocery_task():
    return ("Buy grocery", "Medium", "2024-12-2", [], [], False)

@fixture
def only_description_task():
    return ("Read book", None, None, None, None, None)

@fixture
def no_priority_task():
    return ("Plan trip", None, "2024-12-2", ["vacation"], "Siyuan", False)

@fixture
def no_due_date():
    return ("Finish homework", "High", None, ["school"], "Siyuan", False)

@fixture
def no_tags_task():
    return ("Call doctor", "High", "2024-11-12", None, "Siyuan", False)

@fixture
def no_delegate_task():
    return ("Meeting", "High", "2024-11-22", ["work"], None, False)

@fixture
def no_complete_task():
    return ("Meeting", "High", "2024-11-22", ["work"], None, None)

@fixture
def empty_todolist():
    return TodoList()

@fixture
def one_task_todolist(grocery_task):
    todo_list = TodoList()
    todo_list.tasks = [grocery_task]
    return todo_list

@pytest.fixture
def multiple_task_todolist():
    todo_list = TodoList()
    todo_list.tasks = [
        ("Buy grocery", "Medium", "2024-12-02", [], None, False),
        ("Read book", "High", None, [], None, False)
    ]
    return todo_list

## Functional Tests
def test_add_task_delegate_valid(one_task_todolist, capfd):
    """Test adding a valid delegate to an existing task."""
    # Act
    one_task_todolist.add_task_delegate(1, "Alice")
    
    # Assert: Check console output
    out, err = capfd.readouterr()
    assert "Task delegated to Alice" in out
    
    # Assert: Check task's delegate
    assert one_task_todolist.tasks[0][4] == "Alice"

def test_add_task_delegate_invalid_task_number(multiple_task_todolist, capfd):
    """Test attempting to add a delegate to a non-existent task."""
    # Act
    multiple_task_todolist.add_task_delegate(3, "Alice")
    
    # Assert: Check for error message
    out, err = capfd.readouterr()
    assert "Invalid task number!" in out

def test_add_task_delegate_empty_todolist(empty_todolist, capfd):
    """Test attempting to add a delegate to an empty todo list."""
    # Act
    empty_todolist.add_task_delegate(1, "Alice")
    
    # Assert: Check for error message
    out, err = capfd.readouterr()
    assert "Invalid task number!" in out

## Error Handling
def test_add_task_delegate_invalid_delegate_name(one_task_todolist, capfd):
    """Test adding an invalid delegate name with special characters."""
    # Act
    one_task_todolist.add_task_delegate(1, "Al!ce@123")
    
    # Assert: Check for error message
    out, err = capfd.readouterr()
    assert "Invalid delegate" in out

def test_add_task_delegate_blank_delegate_name(one_task_todolist, capfd):
    """Test adding a blank delegate name."""
    # Act
    one_task_todolist.add_task_delegate(1, "")
    
    # Assert: Check for error message
    out, err = capfd.readouterr()
    assert "Invalid delegate" in out

## Edge Cases
def test_add_task_delegate_multiple_delegations(multiple_task_todolist, capfd):
    """Test reassigning delegate for the same task."""
    # Act
    multiple_task_todolist.add_task_delegate(1, "Alice")
    multiple_task_todolist.add_task_delegate(1, "Bob")
    
    # Assert: Check last delegate update
    assert multiple_task_todolist.tasks[0][4] == "Bob"
    out, err = capfd.readouterr()
    assert "Task delegated to Alice" in out
    assert "Task delegated to Bob" in out

def test_add_task_delegate_large_number_of_tasks(capfd):
    """Test delegating a task in a list of 1000 tasks."""
    # Arrange
    todo_list = TodoList()
    todo_list.tasks = [("Task " + str(i), "Medium", None, [], None, False) for i in range(1, 1001)]
    
    # Act
    todo_list.add_task_delegate(500, "Chris")
    
    # Assert: Check delegate assignment
    assert todo_list.tasks[499][4] == "Chris"
    out, err = capfd.readouterr()
    assert "Task delegated to Chris" in out