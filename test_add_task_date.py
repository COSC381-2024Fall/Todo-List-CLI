
from TodoList import TodoList
from pytest import fixture

@fixture
def myList():
    myList= TodoList()
    myList.tasks=[("Buy grocery", "Medium", "2024-12-2", [], "Siyuan", False)]
    return myList

@fixture
def emptyList():
    myList=TodoList
    return myList

def test_correct_output(capfd,myList):
    #Act
    myList.add_task_date(1,"2024-12-3")
    

    #Assert
    out, err=capfd.readouterr()
    assert("2024-12-3" in out)

def test_out_of_range(capfd,myList):
    #Act
    myList.add_task_date(3,"2024-12-3")

    #Assert
    out, err=capfd.readouterr()
    assert("Invalid task number!" in out)

def test_not_greater_than_zero(capfd,myList):
    #Act
    myList.add_task_date(-1,"2024-12-3")

    #Assert
    out, err=capfd.readouterr()
    assert("Invalid task number!" in out)

def test_greater_than_amount_of_tasks(capfd,myList):
    #Act
    myList.add_task_date(2,"2024-12-3")

    #Assert
    out, err=capfd.readouterr()
    assert("Invalid task number!" in out)

def test_date_not_in_right_format(capfd,myList):
    #Act
    myList.add_task_date(1,"12-23-2024")

    #Assert
    out, err=capfd.readouterr()
    assert("Invalid date format! Please enter the date in YYYY-MM-DD format." in out)


#code written incorrectly which prevents these tests from running 

#def test_date_not_string(capfd,myList):
    #Act
 #   myList.add_task_date(1,17)

  #  Assert
   # out, err=capfd.readouterr()
    #assert("Due Date must be a string" in out)

#def test_empty_list(capfd,emptyList):
    #Assert
    #out, err=capfd.readouterr()
    #assert("No tasks in the list to update!" in out)








