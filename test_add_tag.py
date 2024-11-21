# import pytest
from pytest import fixture, raises
from TodoList import TodoList

@fixture
def myList():
    myList = TodoList()
    myList.tasks = [
        ("Buy groceries", "Medium", "2024-12-02", [], "Siyuan", False),
        ("Complete assignment", "High", "2024-11-20", ["urgent"], "Maksim", False)
    ]
    return myList

def test_add_tag_correct_output(capfd, myList):
    # Act
    myList.add_tag(1, "errand")

    # Assert
    out, err = capfd.readouterr()
    assert "Task updated:" in out
    assert "errand" in out  # Verify that the tag is in the output

def test_add_tag_updates_task_state(myList):
    # Act
    myList.add_tag(2, "important")

    # Assert
    task = myList.tasks[1]
    assert "important" in task[3]  # Ensure 'important' is added to the tags

def test_no_tasks_to_add_tag(capfd):
    # Arrange
    empty_list = TodoList()

    # Act
    empty_list.add_tag(1, "new tag")

    # Assert
    out, err = capfd.readouterr()
    assert "No tasks in the list to add a tag!" in out

def test_invalid_task_number_below_range(capfd, myList):
    # Act
    myList.add_tag(0, "invalid_tag")

    # Assert
    out, err = capfd.readouterr()
    assert "Invalid task number!" in out

def test_invalid_task_number_above_range(capfd, myList):
    # Act
    myList.add_tag(3, "invalid_tag")

    # Assert
    out, err = capfd.readouterr()
    assert "Invalid task number!" in out

def test_non_tuple_task_raises_exception():
    # Arrange
    invalid_list = TodoList()
    invalid_list.tasks = ["Non-tuple task"]

    # Act & Assert
    with raises(Exception) as excinfo:
        invalid_list.add_tag(1, "tag")
    assert "Internal error: the task is not a tuple." in str(excinfo.value)

def test_edge_case_empty_string_tag(myList):
    # Act
    myList.add_tag(1, "")

    # Assert
    task = myList.tasks[0]
    assert "" in task[3]  # Ensure an empty tag is added

def test_edge_case_special_characters_tag(myList):
    # Act
    myList.add_tag(1, "!@#$%^")

    # Assert
    task = myList.tasks[0]
    assert "!@#$%^" in task[3]  # Ensure special characters are handled