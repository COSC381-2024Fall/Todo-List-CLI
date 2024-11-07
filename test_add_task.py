from todo import TodoList
from pytest import fixture

@fixture
def grocery_task():
    return ("Buy grocery", "Medium", "2024-12-2", [], "Siyuan", False)

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

## Functional Tests (Basic Cases)
def test_add_a_task(empty_todolist, capfd):
    """Test add a task to an empty todo list
    """
    ## Arrange

    ## Act
    empty_todolist.add_task("Plan trip", "Medium", "2024-12-02")
    
    ## Assert
    ### behavioral
    out, err = capfd.readouterr()
    assert("Plan trip" in out)
    assert("Medium" in out)
    assert("2024-12-02" in out)
    
    ### states
    assert(len(empty_todolist.tasks) == 1)
    task_description, priority, due_date, tags, delegate, complete = empty_todolist.tasks[0]
    assert(task_description == "Plan trip")
    assert(priority == "Medium")
    assert(due_date == "2024-12-02")
    assert(len(tags) == 0)
    assert(delegate is None)
    assert(complete == False)

def test_leading_whitespace(empty_todolist):
    # Arrange
    white_space_task = "     task1     new"

    # Act
    empty_todolist.add_task(white_space_task)

    # Assert
    assert(len(empty_todolist.tasks) == 1)
    task_description, priority, due_date, tags, delegate, complete = empty_todolist.tasks[0]
    # assert(task_description == "task1")
    assert(task_description == white_space_task.strip())

    # Cleanup


    ###
    ### Edge cases: add 1000 tasks, 10k, 100k