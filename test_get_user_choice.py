from todo import *
from pytest import fixture
import random
from io import StringIO
import sys

# Arrange
@fixture
def get_within_range_choice():
    return random.randint(1, 13)

# Arrange
@fixture
def get_out_of_range_choice():
    return random.randint(14, 99)

# Arrange
@fixture
def get_mistype_choice():
    return random.random()

# Arrange
@fixture
def get_empty_choice():
    return " "

def test_get_user_choice_within_range(get_within_range_choice):
    # Save the original stdin
    original_stdin = sys.stdin
    
    # Create a new StringIO object with the inputs
    sys.stdin = StringIO(str(get_within_range_choice))
    
    # Act
    choice = get_user_choice()
    
    # Assert
    assert(choice != None)
    assert((int)(choice) == choice)
    assert(choice >= 1 & choice <= 13)

def test_get_user_choice_out_of_range(get_out_of_range_choice):
    # Save the original stdin
    original_stdin = sys.stdin
    
    # Create a new StringIO object with the inputs
    sys.stdin = StringIO(str(get_out_of_range_choice))
    
    # Act
    choice = get_user_choice()
    
    # Assert
    assert(None == choice)
    
def test_get_user_choice_mistype(get_mistype_choice):
    # Save the original stdin
    original_stdin = sys.stdin
    
    # Create a new StringIO object with the inputs
    sys.stdin = StringIO(str(get_mistype_choice))
    
    # Act
    choice = get_user_choice()
    
    # Assert
    assert(None == choice)

def test_get_empty_user_choice(get_empty_choice):
    # Save the original stdin
    original_stdin = sys.stdin
    
    # Create a new StringIO object with the inputs
    sys.stdin = StringIO(str(get_empty_choice))
    
    # Act
    choice = get_user_choice()
    
    # Assert
    assert(None == choice)