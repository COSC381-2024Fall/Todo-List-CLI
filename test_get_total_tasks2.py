from TodoList import TodoList
from pytest import fixture

def test_empty_tasks():
    #arrange
    todo_list = TodoList()
    
    #assert
    assert todo_list.get_total_tasks() == 0
    
def test_one():
    #arrange
    todo_list = TodoList()
    todo_list.tasks = [("Homework", "High", "2024-11-15")]
    
    #assert
    assert todo_list.get_total_tasks() == 1


def test_large():
    #arrange
    todo_list = TodoList()
    for i in range(1000):
        todo_list.add_task(f"Task {i}")
    
    #assert
    assert todo_list.get_total_tasks() == 1000
    
def test_deletion():
    #arrange
    todo_list = TodoList()
    todo_list.tasks = [("Homework"), ("Shopping"), ("Car Service")]
    
    #act
    todo_list.delete_task(2)
    
    #assert
    assert todo_list.get_total_tasks() == 2
    
def test_all_deletion():
    #arrange
    todo_list = TodoList()
    for i in range(1000):
        todo_list.add_task(f"Task {i}")
        
    #act
    todo_list.delete_all_tasks()
    
    #assert
    assert todo_list.get_total_tasks() == 0
    