from todo import TodoList
from pytest import fixture

#Arrange - Setting up
@fixture
def populated_todolist():
    todo_list = TodoList()
    todo_list.tasks = [
        ("Buy grocery", "Medium", "2024-12-02", [], "Long", False),
        ("Call doctor", "High", "2024-11-12", [], "Long", False),
        ("Finish homework", "High", None, ["school"], "Long", False)
    ]
    return todo_list

@fixture
def empty_todolist():
    return TodoList()

#Act

# function to add a task
def add_sample_task(todo_list, task_name="Read book", priority="Low", due_date="2024-12-10"):
    todo_list.add_task(task_name, priority, due_date)

# Assert

#Deletion
def test_delete_task_valid_number(capfd, populated_todolist):
    task_number = 2  
    populated_todolist.delete_task(task_number)
    out, err = capfd.readouterr()
    
    assert len(populated_todolist.tasks) == 2
    assert "Task removed" in out
    assert "Call doctor" in out

def test_delete_task_invalid_number_zero(capfd, populated_todolist):
    task_number = 0
    populated_todolist.delete_task(task_number)
    out, err = capfd.readouterr()
    
    assert len(populated_todolist.tasks) == 3
    assert "Invalid task number!" in out

def test_delete_task_invalid_number_negative(capfd, populated_todolist):
    task_number = -1
    populated_todolist.delete_task(task_number)
    out, err = capfd.readouterr()
    
    assert len(populated_todolist.tasks) == 3
    assert "Invalid task number!" in out

def test_delete_task_invalid_number_exceeds(capfd, populated_todolist):
    task_number = len(populated_todolist.tasks) + 1  
    populated_todolist.delete_task(task_number)
    out, err = capfd.readouterr()
    
    assert len(populated_todolist.tasks) == 3
    assert "Invalid task number!" in out
