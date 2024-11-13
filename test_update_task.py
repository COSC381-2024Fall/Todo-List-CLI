#This file provides testing for the update_task method in TodoList.py

#There are the following tests...
#testing that output contains new task name - PASSES
#test for empty list case - PASSES
#test for task number outside of range of number of tasks - PASSES
#test for task number less than 0 - PASSES
#test for a task number that is not an integer - FAILS
#test empty task - FAILS

from todo import TodoList
from pytest import fixture

@fixture
def myList():
    #Arrange
    myList = TodoList()
    myList.tasks = [("Buy grocery", "Medium", "2024-12-2", [], "Siyuan", False)]
    return myList

#testing that output contains new task name
def test_correct_output(capfd, myList):
    #Arrange

    #Act
    myList.update_task(1, "New Name")

    #Assert
    out, err = capfd.readouterr()
    assert("New Name" in out)

#testing error messages
#test for empty list case
def test_empty_list(capfd):
    #Arrange
    myList = TodoList() #new empty list 
    #Act
    myList.update_task(1, "New Name")

    #Assert
    out, err = capfd.readouterr()
    assert("No tasks in the list to update!" in out)

#test for invalid task number - outside of range of number of tasks
def test_invalid_task_number(capfd, myList):
    #Arrange

    #Act
    myList.update_task(2, "New Name") #2 is outside of the range of number of tasks

    #Assert
    out, err = capfd.readouterr()
    assert("Invalid task number!" in out)

#test for invalid task number - less than 0
def test_invalid_task_number_negative(capfd, myList):
    #Arrange

    #Act
    myList.update_task(-1, "New Name") #-1 is not greater than 0

    #Assert
    out, err = capfd.readouterr()
    assert("Invalid task number!" in out)

#test for a invalid task number - that is not an integer
def test_noninteger_task_number(capfd, myList):
    #Arrange

    #Act
    myList.update_task("k", "New Name") #k is not an integer

    #Assert
    out, err = capfd.readouterr()
    assert("Invalid" in out)

#test empty task
def test_empty_task(myList):
    #Arrange

    #Act
    myList.update_task(1, "") #"" is an empty string

    #Assert
    task_name = myList.tasks[0][0]
    assert task_name != ""