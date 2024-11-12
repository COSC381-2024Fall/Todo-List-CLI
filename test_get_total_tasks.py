from TodoList import TodoList
from pytest import fixture

def test_empty_list():
    # arrange
    myList = TodoList()
    myList.tasks = []

    # act
    num = myList.get_total_tasks()

    # assert
    assert(num==0)

def test_one_task_list():
    # arrange
    oneList = TodoList()
    oneList.tasks = [("Buy grocery", "Medium", "2024-12-2", [], "Siyuan", False)]

    # act
    num = oneList.get_total_tasks()

    # assert
    assert(num==1)

def test_two_tasks():
    # arrange
    twoList = TodoList()
    twoList.tasks = [("Buy grocery", "Medium", "2024-12-2", [], "Siyuan", False), ("Read book", None, None, None, None, None)]

    # act
    num = twoList.get_total_tasks()

    # assert
    assert(num==2)

def test_three_tasks():
    # arrange
    threeList = TodoList()
    threeList.tasks= [("Buy grocery", "Medium", "2024-12-2"), ("Guy grocery", "Medium", "2024-10-2"), ("Buy eggs", "Medium", "2023-12-2")]

    # act
    num = threeList.get_total_tasks()

    # assert
    assert(num==3)

def test_four_tasks():
    # arrange
    fouList = TodoList()
    fouList.tasks = [("Buy grocery", "Medium", "2024-12-2"), ("Buy", "Medium", "2024-11-2"), ("Walk", "Medium", "2024-12-8"), ("Run", "Medium", "2024-12-3")]

    # act
    num = fouList.get_total_tasks()

    # assert
    assert(num==4)

