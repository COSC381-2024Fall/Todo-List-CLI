from todo import TodoList
from pytest import fixture

@fixture
def empty_todolist():
    return TodoList()

@fixture
def grocery_task():
    return ("Buy grocery", "Medium", "2024-12-02", [], "Holman", False)

@fixture
def gym_task():
    return ("Go to gym", "Medium", "2024-12-02", [], "Holman", False)

@fixture
def gym_task1():
    return ("go to gym", "Medium", "2024-12-02", [], "Holman", False)

@fixture
def gym_task2():
    return ("Ñ Go to gym", "Medium", "2024-12-02", [], "Holman", False)

@fixture
def num_task1():
    return ("1 go to gym", "Medium", "2024-12-02", [], "Holman", False)

@fixture
def num_task2():
    return ("2 go to gym", "Medium", "2024-12-02", [], "Holman", False)

@fixture
def one_task_todolist(grocery_task):
    todo_list = TodoList()
    todo_list.tasks = [grocery_task]
    return todo_list

@fixture
def two_task_todolist(grocery_task, gym_task):
    todo_list = TodoList()
    todo_list.tasks = [grocery_task, gym_task]
    return todo_list

@fixture
def two_task_todolist_num(num_task1, num_task2):
    todo_list = TodoList()
    todo_list.tasks = [num_task1, num_task2]
    return todo_list

@fixture
def two_task_todolist_ooo(gym_task, grocery_task):
    todo_list = TodoList()
    todo_list.tasks = [gym_task, grocery_task]
    return todo_list

@fixture
def two_task_todolist_non_english(gym_task2, grocery_task):
    todo_list = TodoList()
    todo_list.tasks = [gym_task2, grocery_task]
    return todo_list

@fixture
def two_task_todolist_lower(gym_task1, grocery_task):
    todo_list = TodoList()
    todo_list.tasks = [gym_task1, grocery_task]
    return todo_list

@fixture
def two_task_todolist_lower_ooo(grocery_task, gym_task1):
    todo_list = TodoList()
    todo_list.tasks = [grocery_task, gym_task1]
    return todo_list

def test_list_tasks_alphabetic_normal(two_task_todolist, capfd):
    """Test alphabatize on a normal pre sorted todo list
    """
    ## Arrange

    ## Act
    two_task_todolist.list_tasks_alphabetic()
    
    ## Assert
    
    assert(len(two_task_todolist.tasks) == 2)

    out, err = capfd.readouterr()
    out = out.splitlines()
    
    assert("Buy grocery" in out[0])
    assert("Go to gym" in out[1])

def test_list_tasks_alphabetic_out_of_order(two_task_todolist_ooo, capfd):
    """Test alphabatize on a normal todo list non sorted
    """
    ## Arrange

    ## Act
    two_task_todolist_ooo.list_tasks_alphabetic()
    
    ## Assert
    assert(len(two_task_todolist_ooo.tasks) == 2)

    out, err = capfd.readouterr()
    out = out.splitlines()

    assert("Buy grocery" in out[0])
    assert("Go to gym" in out[1])

def test_list_tasks_alphabetic_capitalised(two_task_todolist_lower, capfd):
    """Test alphabatize on a todo list with 1 task capitalised but pre sorted
    """
    ## Arrange

    ## Act
    two_task_todolist_lower.list_tasks_alphabetic()
    
    ## Assert
    assert(len(two_task_todolist_lower.tasks) == 2)

    out, err = capfd.readouterr()
    out = out.splitlines()

    assert("Buy grocery" in out[0])
    assert("go to gym" in out[1])

def test_list_tasks_alphabetic_capitalised_ooo(two_task_todolist_lower_ooo, capfd):
    """Test alphabatize on a todo list with 1 task capitalised and out of order
    """
    ## Arrange

    ## Act
    two_task_todolist_lower_ooo.list_tasks_alphabetic()
    
    ## Assert
    assert(len(two_task_todolist_lower_ooo.tasks) == 2)

    out, err = capfd.readouterr()
    out = out.splitlines()

    assert("Buy grocery" in out[0])
    assert("go to gym" in out[1])

def test_list_tasks_alphabetic_num(two_task_todolist_num, capfd):
    """Test alphabatize on a todo list with numbers involved
    """
    ## Arrange

    ## Act
    two_task_todolist_num.list_tasks_alphabetic()
    
    ## Assert
    
    assert(len(two_task_todolist_num.tasks) == 2)

    out, err = capfd.readouterr()
    out = out.splitlines()
    
    assert("1 go to gym" in out[0])
    assert("2 go to gym" in out[1])

def test_list_tasks_alphabetic_non_english(two_task_todolist_non_english, capfd):
    """Test alphabatize on a todo list with non english chars
    """
    ## Arrange

    ## Act
    two_task_todolist_non_english.list_tasks_alphabetic()
    
    ## Assert
    
    assert(len(two_task_todolist_non_english.tasks) == 2)

    out, err = capfd.readouterr()
    out = out.splitlines()
    
    assert("Buy grocery" in out[0])
    assert("Ñ Go to gym" in out[1])