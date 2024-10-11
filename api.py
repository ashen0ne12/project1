import requests

def test_get_users():
    url = "https://jsonplaceholder.typicode.com/users"

    response = requests.get(url)


    assert response.status_code == 200

    users = response.json()


    assert len(users) > 0


    for user in users:
        assert "id" in user
        assert "name" in user
        assert "username" in user
        assert "email" in user


        assert "@" in user["email"]
