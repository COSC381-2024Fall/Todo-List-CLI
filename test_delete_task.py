from pytest import fixture
from TodoList import TodoList

@fixture
def task1():
    return ("Buy grocery", "Medium", "2024-12-2", [], None, False)

@fixture
def task2():
    return ("Turn in Lab", "High", "2024-12-3", [], None, False)

@fixture
def myList(task1, task2):
    myList = TodoList()
    myList.tasks = [task1, task2]
    return myList

@fixture
def myEmptyList():
    myList = TodoList()
    return myList

def test_normal_deleting_task(capfd, myList):
    #Arrange
    
    #Act
    myList.delete_task(1)
    #Assert
    out, err = capfd.readouterr()
    assert(len(myList.tasks)==1)
    assert("Buy grocery" in out)
    assert("Medium" in out)
    assert("2024-12-2" in out)

def test_empty_list_delete(capfd, myEmptyList):
    #Arrange
    
    #Act
    myEmptyList.delete_task(1)
    #Assert
    out, err = capfd.readouterr()
    assert("No tasks in the list to delete!" in out)

def test_out_of_range_delete(capfd, myList):
    #Arrange
    
    #Act
    myList.delete_task(3)
    #Assert
    out, err = capfd.readouterr()
    assert("Invalid task number!" in out)
