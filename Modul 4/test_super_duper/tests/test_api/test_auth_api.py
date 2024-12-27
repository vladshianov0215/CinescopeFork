import requests

def test_login_user():
    url = "https://auth.dev-cinescope.store/login"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json"
    }
    data = {
        "email": "kekzurruh@gmail.com",
        "password": "rVloAvM3TB"
    }
    response = requests.post(url, json=data, headers=headers)

    # Проверки
    assert response.status_code == 200, "Логин должен быть успешным"
    response_data = response.json()
    assert "accessToken" in response_data, "Ответ должен содержать accessToken"
    assert response_data["user"]["email"] == data["email"], "Email в ответе должен совпадать"






