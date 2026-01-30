# pip install pytest
# pip install pytest-mock 

# ___ Cases ___
# assert
# with pytest.raises()
# Fixtures
# Fixtures teardown
# Parametarize
# mocking

# ______________ PYTEST EXAMPLES ______________
import pytest

#-> 1. assert 
from example import check_weather
def test_check_weather():
    assert check_weather(21) == "hot"
    assert check_weather(20) == "cold"
    assert check_weather(19) == "cold"
    assert check_weather(0) == "super_cold"


# -> 2. pytest.raises
from simple_arith import add, divide
def test_add():
    assert add(3,5) == 8, "Sum of 3 and 5 should be 8"
    assert add(-2, -4) == -6 , "Sum of -2 and -4 should be -6"

def test_divide():
    with pytest.raises(ZeroDivisionError, match="Cannot divide by 0"):
        divide(10,0)


#-> 3. pytest.fixtures
from user_manager import User
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


#-> 4. pytest.mark.parametrize
from is_prime import is_prime
@pytest.mark.parametrize("num, expected", [
    (1, False),
    (2, True),
    (3, True),
    (4, False),
    (5, True)
])
def test_prime(num, expected):
    assert is_prime(num) == expected 
 

#-> 5. pytest.fixture with yield and data clear at last
from db import Database
@pytest.fixture
def db():
    '''PRovides instance of the Database class and cleans up after the test'''
    database = Database()
    yield database  #Provides the fixture instance
    database.data.clear()    #Clean up step - not needed for in-memoyry but useful in real db

def test_add_user(db):
    db.add_user(1, "Ethan")
    assert db.get_user(1) == "Ethan"

def test_add_duplicate_user(db):
    db.add_user(1, "Ethan")
    with pytest.raises(ValueError, match="User already exists"):
        assert db.add_user(1, "Nitin")

def test_delete_user(db):
    db.add_user(2, "Nitin")
    db.delete_user(2)
    assert db.get_user(2) is None


#-> 6. pytest - mocker.patch
from weather import get_weather_data
def test_get_weather_data(mocker):
    mock_get = mocker.patch("weather.requests.get")
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {"temperature": 25, "condition": "sunny"}
    result = get_weather_data("Dubai")
    assert result == {"temperature": 25, "condition": "sunny"}
    mock_get.assert_called_once_with("https://api.weather.com/v1/Dubai")

#-> 7. pytest - mocker.patch and assert_called_once_with
from sql_lite import save_user
def test_save_user(mocker):
    mock_conn = mocker.patch("sqlite3.connect")
    mock_cursor = mock_conn.return_value.cursor.return_value
    save_user("Nitin", 31)
    mock_conn.assert_called_once_with("users.db")
    mock_cursor.execute.assert_called_once_with("INSERT INTO users (name, age) VALUES (?, ?)", ("Nitin", 31))

# 8. pytest - mocker.Mock() with spec
from api_client import UserService, APIClient
def test_get_username_with_mock(mocker):
    mock_api_client = mocker.Mock(spec=APIClient)

    mock_api_client.get_user_data.return_value = {"id": 1,"name": "Ethan"}
    service = UserService(mock_api_client)
    result = service.get_user_name(1)

    assert result == "ETHAN"
    mock_api_client.get_user_data.assert_called_once_with(1)

#-> 9. pytest.fixture for api testing
from flask_api import app
@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client

def test_add_user(client):
    response = client.post('/users', json={"id": 1, "name": "Ethan"})
    assert response.status_code == 201
    assert response.json == {"id": 1, "name": "Ethan"}

def test_get_user(client):
    client.post('/users', json={"id": 2, "name": "Nitin"})
    response = client.get('/users/2')
    assert response.status_code==200
    assert response.json=={"id": 2, "name": "Nitin"}