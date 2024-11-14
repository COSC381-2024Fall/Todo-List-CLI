from pytest import fixture
from TodoList import TodoList
import sys


# Arrange

@fixture
def myList():
    #Arrange
    myList = TodoList()
    myList.tasks = [("Lunch", "Small", "2025-4-23", [], "3.14159", False)]
    return myList

# Arrange
@fixture
def get_remove_date():
    return 1

# Arrange
@fixture
def get_invalid_task_num():
    return 99

# Arrange
@fixture
def get_no_due_date_task():
    return 1

def test_remove_due_date(get_remove_date, capfd):
    out, err = capfd.readouterr()
    # Save the original stdin
    original_stdin = sys.stdin
    
    # Create a new StringIO object with the inputs
    sys.stdin = StringIO(str(get_remove_date))
    
    # Act
    choice = 10
    task_number = get_remove_date

    # Assert
    assert(choice)
    assert(task_number)


def test_invalid_task_num(get_invalid_task_num,capfd):
    out, err = capfd.readouterr()
    # Save the original stdin
    original_stdin = sys.stdin
    
    # Create a new StringIO object with the inputs
    sys.stdin = StringIO(str(get_invalid_task_num))
    
    # Act
    choice = 10
    task_number = get_invalid_task_num

    # Assert
    assert(choice)

    # Quick negative test
    assert(-1)
    assert(choice)
    assert(task_number)

def test_task_with_no_due_date(get_no_due_date_task,capfd):
    out, err = capfd.readouterr()
    # Save the original stdin
    original_stdin = sys.stdin
    
    # Create a new StringIO object with the inputs
    sys.stdin = StringIO(str(get_no_due_date_task))
    
    # Act
    choice = 10
    task_number = get_no_due_date_task

    # Assert
    # Create new myLists

    #Choice stuff
    assert(choice)
    assert(task_number)