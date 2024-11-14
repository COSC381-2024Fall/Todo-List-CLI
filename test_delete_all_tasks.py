from todo import TodoList
from pytest import fixture
from unittest.mock import patch



# we need minimal tests for adding, since there are other test files for them. 
#i think testing a normal task, and an empty one would be sufficient, update:
#added another task for the 2 task list as it checks for duplicates
@fixture 
def homework_task():
    return "do homework"

@fixture 
def empty_task():
    return ""

@fixture
def laundry_task():
    return "fold clothes"

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
def two_task_list(homework_task, laundry_task):
    todo_list = TodoList()
    todo_list.add_task(homework_task)
    todo_list.add_task(laundry_task)
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
    no_tasks_list.delete_all_tasks() # now delete again
    assert captured.out == "No tasks to delete.\n" # ensure the second delete also worked as expected 
    assert no_tasks_list.tasks == []

def test_delete_twice_one(one_task_list, capsys):
    # arrange / act
    one_task_list.delete_all_tasks()
    # check output for correctness
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
    one_task_list.delete_all_tasks() #deletes, adds then deletes again and ensures nothing in list
    one_task_list.add_task(homework_task)
    one_task_list.delete_all_tasks()
    assert one_task_list.tasks == []

def test_delete_add_delete_two(homework_task, two_task_list):
    two_task_list.delete_all_tasks() #deletes, adds then deletes, then asserts nothing in list
    two_task_list.add_task(homework_task)
    two_task_list.delete_all_tasks()
    assert two_task_list.tasks == []

def test_delete_add_delete_empty(homework_task, no_tasks_list):
    no_tasks_list.delete_all_tasks() #empty the empty list
    no_tasks_list.add_task(homework_task) #empty homework then delete again and asserts
    no_tasks_list.delete_all_tasks()
    assert no_tasks_list.tasks == []

def test_large_task_list_deletion(homework_task):
    todo_list = TodoList()
    for i in range(1000):  #loops 1000 times to ensure 1000 unique tasks added
       unique_task = homework_task + str(i)  #makes new tasks off of hw task
       todo_list.add_task(unique_task) # adds each unique task
    assert todo_list.get_total_tasks() == 1000 # checks 1000 got added then deleted correctly
    todo_list.delete_all_tasks()
    assert todo_list.tasks == []

def test_delete_with_new_task_added(homework_task, two_task_list, capsys):
    two_task_list.delete_all_tasks()  # Delete all tasks
    captured = capsys.readouterr()
    assert captured.out == "All tasks deleted.\n"
    assert two_task_list.tasks == []
    
    # Add a new task after deletion
    two_task_list.add_task(homework_task)
    assert two_task_list.get_total_tasks() == 1  # Ensure the task was added correctly
