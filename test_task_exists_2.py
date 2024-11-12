from todo import TodoList
from pytest import fixture

# Testing for task_exists()

@fixture
def grocery_task():
    return ("Buy grocery", "Medium", "2024-12-2", [], "Siyuan", False)

@fixture
def no_due_date():
    return ("Finish homework", "High", None, ["school"], "Siyuan", False)

@fixture
def empty_task():
    return ("", "Medium")

@fixture
def white_space_task():
    return ("   ", "Low")

@fixture
def empty_todolist():
    return TodoList()

@fixture
def two_task_todolist(grocery_task, no_due_date):
    todo_list = TodoList()
    todo_list.tasks = [grocery_task, no_due_date]
    return todo_list
    

def test_valid_task_exists(two_task_todolist, capfd):
    # Assert
    out, err = capfd.readouterr()
    assert(two_task_todolist.task_exists("Buy Grocery") == 1)
    assert(two_task_todolist.tasks[0][0].lower() ==  "Buy Grocery".lower())
    assert(two_task_todolist.task_exists("Finish Homework") == 2)
    assert(two_task_todolist.tasks[1][0].lower() ==  "Finish Homework".lower())
    assert(two_task_todolist.task_exists("FINISH HOMEWORK   ") == 2)

def test_correct_index(two_task_todolist, capfd):
    out, err = capfd.readouterr()
    assert(two_task_todolist.tasks[0][0].lower() ==  "Buy Grocery".lower())
    assert(two_task_todolist.tasks[1][0].lower() ==  "Finish Homework".lower())

def test_leading_whitespace(two_task_todolist, capfd):
    # Assert
    out, err = capfd.readouterr()
    assert(two_task_todolist.task_exists("    buy grocery") == 1)
    assert(two_task_todolist.task_exists("    Finish Homework") == 2)

def test_non_existent_task(empty_todolist, capfd):
    notATask = "A task that doesn't exist"

    out, err = capfd.readouterr()
    assert(empty_todolist.task_exists(notATask) == None)

def test_empty_string(empty_todolist, capfd):
    emptyTask = ""
    empty_todolist.add_task(emptyTask)

    out, err = capfd.readouterr()
    assert(empty_todolist.task_exists(emptyTask) == 1)