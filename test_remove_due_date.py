from todo import TodoList
from pytest import fixture

@fixture
def myList():
    #Arrange
    myList = TodoList()
    myList.tasks = [("Buy grocery", "Medium", "2024-12-2", [], "Siyuan", False)]
    return myList


def test_remove_due_date(capfd, myList):
    #Act
    myList.remove_due_date(1)
    
    #Assert
    out, err = capfd.readouterr()
    assert("Due date removed from task: Buy grocery\n" in out)

def test_empty_list(myList):
    # Act
    myList.tasks =[]
    
    # Assert if list is empty
    assert myList.tasks == []