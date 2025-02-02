from Modul_4.Cinescope.custom_requester.custom_requester import CustomRequester
from Modul_4.Cinescope.constants import LOGIN_ENDPOINT, REGISTER_ENDPOINT

class AuthAPI(CustomRequester):
    """
    Класс для работы с аутентификацией.
    """

    def __init__(self, session):
        # Используем super(), чтобы передать сессию и базовый URL
        super().__init__(session=session, base_url="https://auth.dev-cinescope.coconutqa.ru/")

    def register_user(self, user_data):
        """Регистрирует нового пользователя"""
        return self.send_request("POST", REGISTER_ENDPOINT, data=user_data)

    def login_user(self, login_data):
        """Авторизует пользователя и получает токен"""
        return self.send_request("POST", LOGIN_ENDPOINT, data=login_data)

    def change_user_role(self, user_id, new_roles, admin_token):
        """Изменяет роль пользователя"""
        headers = {"Authorization": f"Bearer {admin_token}"}
        data = {"roles": new_roles}
        return self.send_request("PATCH", f"/user/{user_id}", data=data, headers=headers)

    def delete_user(self, user_id, admin_token):
        """Удаляет пользователя (только для ADMIN и SUPER_ADMIN)"""
        headers = {"Authorization": f"Bearer {admin_token}"}
        return self.send_request("DELETE", f"/user/{user_id}", headers=headers, expected_status=[200, 204, 404])

    def get_user(self, user_id, admin_token):
        """
        Получение информации о пользователе.
        """
        headers = {"Authorization": f"Bearer {admin_token}"}  # ✅ Добавили авторизацию
        response = self.send_request(
            method="GET",
            endpoint=f"/user/{user_id}",
            headers=headers,  # ✅ Передаем заголовки
            expected_status=[200]
        )
        return response.json()

    def login(self, email, password):
        """
        Логин пользователя.
        """
        response = self.send_request(  # ✅ Убрал self.requester
            method="POST",
            endpoint="/login",
            data={"email": email, "password": password},
            expected_status=[201]
        )
        return response.json()