from todo import print_menu
from pytest import fixture

# Predefined menu tasks
menu_tasks_naked = [
    "To-Do List CLI App",
    "Add task",
    "List tasks ordered numerically",
    "List tasks ordered alphabetically",
    "Delete task",
    "Add/Update a due date to a task",
    "Add/Update a tag to a task",
    "Delete all tasks",
    "Edit task description",
    "Show total number of tasks",
    "Delete a due date to a task",
    "Delegate task to someone else",
    "Mark Task Complete",
    "Quit",
]

menu_tasks_numbered = ["To-Do List CLI App"] + [f"{i}. {task}" for i, task in enumerate(menu_tasks_naked[1:], 1)]

# Fixtures
@fixture
def tasks_count():
    return len(menu_tasks_naked)

@fixture
def entire_menu():
    return f'\n{"\n".join(menu_tasks_numbered)}\n'

## Tests
def test_print_menu_basic(tasks_count, capfd):
    print_menu()
    out, err = capfd.readouterr()

    # Verify all tasks are listed correctly
    for i in range(1, tasks_count):
        assert str(i) in out, f'Missing Task {i}'
    assert tasks_count == len(out.strip().split('\n'))

def test_print_menu_with_tasks_added(capfd):
    from todo import TodoList
    todo = TodoList()
    todo.add_task("Test Task 1")
    todo.add_task("Test Task 2")

    print_menu()
    out, err = capfd.readouterr()

    assert "Test Task 1" in out
    assert "Test Task 2" in out

def test_print_menu_after_task_deletion(capfd):
    from todo import TodoList
    todo = TodoList()
    todo.add_task("Test Task 1")
    todo.delete_task(1)

    print_menu()
    out, err = capfd.readouterr()

    assert "Test Task 1" not in out

def test_print_menu_empty_list(capfd):
    from todo import TodoList
    todo = TodoList()
    todo.delete_all_tasks()

    print_menu()
    out, err = capfd.readouterr()

    assert "No tasks in the list!" in out

def test_print_menu_with_due_dates_and_tags(capfd):
    from todo import TodoList
    todo = TodoList()
    todo.add_task("Test Task 1", date="2024-12-25")
    todo.add_tag(1, "Urgent")

    print_menu()
    out, err = capfd.readouterr()

    assert "Test Task 1 (Due: 2024-12-25)" in out
    assert "Urgent" in out

def test_print_menu_invalid_task(capfd):
    from todo import TodoList
    todo = TodoList()
    todo.add_task("Test Task 1")
    todo.delete_task(999)  # Invalid task number

    print_menu()
    out, err = capfd.readouterr()

    assert "Invalid task number!" in out

def test_print_menu_with_priority(capfd):
    from todo import TodoList
    todo = TodoList()
    todo.add_task("High Priority Task", priority="High")

    print_menu()
    out, err = capfd.readouterr()

    assert "High Priority Task [Priority: High]" in out
