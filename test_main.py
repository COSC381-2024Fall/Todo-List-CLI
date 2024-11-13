import pytest #imports whole module
#from pytest import fixture #imports specific element from module
import todo
import TodoList
from unittest.mock import patch

#@fixture

#tests if no answer is provided
def testInvalidMenuOption(capfd):
    #Arrange
    #Prepare expected output
    expectedOutput = "Invalid choice! Please choose a valid option."
    
    #Act
    #Simuilate user input as empty string
    with patch("builtins.input", side_effect=["", 13]):
        #Runs the main
        todo.main()
    
    #Assert 
    #Capture the output and strip whitespace
    out, err = capfd.readouterr()
    out = out.strip()

    #Debugging test to verify output
    #print("Expected output: ", repr(expectedOutput))
    #print("Actual output: ", repr(out))
    assert expectedOutput in out.strip() 

#Tests the exception handling when adding a task
def testMenuAddTask(capfd):
    #Arrange
    invalidYesNo = "Invalid input. Please enter '1' for Yes or '2' for No."
    invalidDate = "Invalid date format. Please enter the date in YYYY-MM-DD format."
    invalidPriority = "Invalid priority. Please enter 'Low', 'Medium', or 'High'."

    #Act
    #Simuilate user input 
    with patch("builtins.input", side_effect=["1", "Task1", "Bobby", "1", "9999-85-12", "2024-11-12", "Middle", "Medium", 13]):
        #Runs the main
        todo.main()
    
    #Assert
    #Capture the output
    out, err = capfd.readouterr()
    
    assert invalidYesNo in out
    assert invalidDate in out
    assert invalidPriority in out