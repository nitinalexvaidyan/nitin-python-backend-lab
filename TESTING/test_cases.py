# pip install pytest
# pip install pytest-mock 

# ___ Cases ___
# assert
# with pytest.raises()
# Fixtures
# Fixtures teardown
# Parametarize
# mocking

import pytest
from example import check_weather
from simple_arith import add, divide
from user_manager import User
from is_prime import is_prime

def test_check_weather():
    assert check_weather(21) == "hot"
    assert check_weather(20) == "cold"
    assert check_weather(19) == "cold"
    assert check_weather(0) == "super_cold"

def test_add():
    assert add(3,5) == 8, "Sum of 3 and 5 should be 8"
    assert add(-2, -4) == -6 , "Sum of -2 and -4 should be -6"


def test_divide():
    with pytest.raises(ZeroDivisionError, match="Cannot divide by 0"):
        divide(10,0)


@pytest.fixture
def user_manager():
    '''Create an instance of user manager'''
    return User()

def test_add_user(user_manager):
    assert user_manager.add_user("nitin", "nitin.example.com") == True
    assert user_manager.get_user("nitin") == "nitin.example.com"

def test_add_duplicate_user(user_manager):
    user_manager.add_user("nitin", "nitin.example.com")
    with pytest.raises(ValueError, match="User already exists"):
        user_manager.add_user("nitin", "nitin.example.com")


@pytest.mark.parametrize("num, expected", [
    (1, False),
    (2, True),
    (3, True),
    (4, False),
    (5, True)
])
def test_prime(num, expected):
    assert is_prime(num) == expected 