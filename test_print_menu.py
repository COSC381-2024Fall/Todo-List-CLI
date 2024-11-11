from todo import print_menu
from pytest import fixture



## Prep
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

menu_tasks_numbered = ["To-Do List CLI App"]
for i in range(1, len(menu_tasks_naked)):
    menu_tasks_numbered.append(f"{i}. {menu_tasks_naked[i]}")



## Fixtures
@fixture
def tasks_count():
    return len(menu_tasks_naked)

@fixture
def naked_tasks():
    return menu_tasks_naked

@fixture
def numbered_tasks():
    return menu_tasks_numbered

@fixture
def entire_menu():
    inner = '\n'.join(menu_tasks_numbered)
    return f'\n{inner}\n'



## Functional Tests (Basic Cases)
def test_numbers_only(tasks_count, capfd):
    print_menu()

    out, err = capfd.readouterr()

    for i in range(1,tasks_count):
        assert str(i) in out, f'Missing Task number {i}, incorrectly updated/shifted list of tasks?'

    assert str(tasks_count) not in out, f"New Task No.{tasks_count}, update test_print_menu accordingly"
    assert tasks_count == len(out.strip().split('\n')), f"Unexpected number of lines, perhaps a new tasks or multi-line task?"

def test_naked_tasks(naked_tasks, capfd):
    print_menu()

    out, err = capfd.readouterr()

    for item in naked_tasks:
        assert item in out

def test_numbered_tasks(numbered_tasks, capfd):
    print_menu()

    out, err = capfd.readouterr()

    for item in numbered_tasks:
        assert item in out



## Functional Tests (Edge Cases)
def test_entire_menu(entire_menu, capfd):
    print_menu()
    
    out, err = capfd.readouterr()
    
    assert entire_menu == out
    assert "" == err