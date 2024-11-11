from todo import TodoList
from pytest import fixture

#we need minimal tests for adding, since there are other test files for them. 
#i think testing a normal task, and an empty one would be sufficient
@fixture 
def homework_task():
    return "do homework"

@fixture 
def empty_task():
    return ""

@fixture 
def empty_task_list(empty_task):
    todo_list = TodoList()
    todo_list.add_task(empty_task)
    return todo_list

@fixture 
def no_tasks_list():
    return TodoList()

@fixture 
def one_task_list(homework_task):
    todo_list = TodoList()
    todo_list.add_task(homework_task)
    return todo_list

@fixture
def two_task_list(homework_task):
    todo_list = TodoList()
    todo_list.add_task(homework_task)
    todo_list.add_task(homework_task)
    return todo_list

def test_empty_task(empty_task_list, capsys):
    empty_task_list.delete_all_tasks()
    captured = capsys.readouterr()
    assert captured.out == "All tasks deleted.\n"
    assert empty_task_list.tasks  == []

def test_empty_list(no_tasks_list, capsys):
    # arrange/act
    no_tasks_list.delete_all_tasks()
    #assert
    captured = capsys.readouterr()
    assert captured.out == "No tasks to delete.\n" # this is the output of the function
    assert no_tasks_list.tasks == [] # shows nothing in list

def test_one_task_list(one_task_list, capsys):
    # arrange/act
    one_task_list.delete_all_tasks()
    #assert
    captured = capsys.readouterr()
    assert captured.out == "All tasks deleted.\n" #console logged this message
    assert one_task_list.tasks == [] # these ensure nothing in the list

def test_two_task_list(two_task_list, capsys):
    #arrange / act
    two_task_list.delete_all_tasks()

    # assert
    captured = capsys.readouterr()
    assert captured.out == "All tasks deleted.\n" # console message to be printed
    assert two_task_list.tasks == [] # length of 0s

def test_delete_twice_empty(no_tasks_list, capsys):
    # arrange / act
    no_tasks_list.delete_all_tasks() # delete tasks from empty list once
    
    captured = capsys.readouterr() # ensure delete was successful
    assert captured.out == "No tasks to delete.\n"
    assert no_tasks_list.tasks == []

    no_tasks_list.delete_all_tasks() # now delete twice
    
    
    assert captured.out == "No tasks to delete.\n" # ensure the second delete also worked as expected 
    assert no_tasks_list.tasks == []

def test_delete_twice_one(one_task_list, capsys):
    # arrange / act
    one_task_list.delete_all_tasks()
    # check output for correct 
    captured = capsys.readouterr()
    assert captured.out == "All tasks deleted.\n"
    assert one_task_list.tasks == []

    # rerun deleting and checking 
    one_task_list.delete_all_tasks()
    captured = capsys.readouterr()
    assert captured.out == "No tasks to delete.\n"
    assert one_task_list.tasks == []

def test_delete_twice_two(two_task_list, capsys):
    # arrange / act
    two_task_list.delete_all_tasks()
    # check first deletion is acting correctly
    captured = capsys.readouterr()
    assert captured.out == "All tasks deleted.\n"
    assert two_task_list.tasks == []
    # now testing all facets of the second
    two_task_list.delete_all_tasks()
    captured = capsys.readouterr()
    assert captured.out == "No tasks to delete.\n"
    assert two_task_list.tasks == []


def test_delete_add_delete_one(homework_task, one_task_list):
    one_task_list.delete_all_tasks()
    one_task_list.add_task(homework_task)
    one_task_list.delete_all_tasks()


    
    assert one_task_list.tasks == []

def test_delete_add_delete_two(homework_task, two_task_list):
    two_task_list.delete_all_tasks()
    two_task_list.add_task(homework_task)
    two_task_list.delete_all_tasks()

    assert two_task_list.tasks == []

def test_delete_add_delete_empty(homework_task, no_tasks_list, capsys):
    no_tasks_list.delete_all_tasks()
    no_tasks_list.add_task(homework_task)
    no_tasks_list.delete_all_tasks()

    assert no_tasks_list.tasks == []

def test_large_task_list_deletion(homework_task):
    todo_list = TodoList()
    for _ in range(1000):  # Add the same homework task multiple times
        todo_list.add_task(homework_task)
    todo_list.delete_all_tasks()
    assert todo_list.tasks == []

def test_large_task_empty_deletion(empty_task):
    todo_list = TodoList()
    for _ in range(1000):  # Add the same homework task multiple times
        todo_list.add_task(empty_task)
    todo_list.delete_all_tasks()
    assert todo_list.tasks == []