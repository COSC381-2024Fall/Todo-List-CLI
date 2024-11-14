#import pytest
from pytest import fixture
from todo import TodoList

@fixture
def empty_todolist():
    return TodoList()

@fixture
def myList():
    myList=TodoList()
    myList.tasks = [("Buy grocery"), ("Run errands"), ("Die")]
    return myList

def test_delete_task(myList, capfd):
    # Arrange


    # Act
    myList.delete_task(2)

    #Assert
    out, err = capfd.readouterr()
    assert("Run errands" in out)


def test_empty_todolist(empty_todolist, capfd):
    #Arrange

    #Act
    empty_todolist.delete_task(1)

    #Assert
    out, err = capfd.readouterr()
    assert("No tasks in the list to delete!" in out)

def test_number_outof_range(myList, capfd):
    #Act
    myList.delete_task(4)


    #Assert
    out, err = capfd.readouterr()
    assert("Invalid task number!" in out)

def test_task_deletion(myList):
    #Arrange


    #Act
    initial_count = len(myList.tasks)
    myList.delete_task(3)


    #Assert
    assert(len(myList.tasks)) == initial_count - 1
    

def test_multiple_task_deletion(myList, capfd):
    #Arrange



    #Act
    initial_count = len(myList.tasks)
    myList.delete_task(1)
    myList.delete_task(1)
    myList.delete_task(1)



    #Assert
    out, err = capfd.readouterr()
    assert(len(myList.tasks)) == initial_count - initial_count