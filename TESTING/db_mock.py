from db import add_user

def test_save_user(mocker):
    mock_conn = mocker.patch("sqlite.connect")
    mock_cursor = mock_conn.return_value.cursor.return_value

    save_user("Nitin", 31)
    mock_conn.assert_called_once_with("users.db")
    mock_cursor.execute.assert_called_once_with("INSERT INTO users (name, age) VALUES (?, ?)", ("Nitin", 31))