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

def test_remove_due_date_invalid_id(capfd, myList):
    # Act
    myList.remove_due_date(2)  # Invalid task ID (only 1 task exists)
    
    # Assert
    out, err = capfd.readouterr()
    assert "Invalid task number!" in out

def test_remove_due_date_already_none(capfd, myList):
    # Act
    myList.remove_due_date(1)  # First removal, sets due date to None
    myList.remove_due_date(1)  # Second removal attempt on the same task
    
    # Assert
    out, err = capfd.readouterr()
    assert "This task doesn't have a due date." in out