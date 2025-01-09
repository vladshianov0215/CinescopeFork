from Modul_4.Cinescope.custom_requester.custom_requester import CustomRequester
from Modul_4.Cinescope.constants import USER_INFO_ENDPOINT, DELETE_USER_ENDPOINT

class UserAPI(CustomRequester):
    """
    Класс для работы с API пользователей.
    """
    def get_user_info(self, user_id, expected_status=200):
        """
        Получение информации о пользователе.
        """
        endpoint = USER_INFO_ENDPOINT.format(user_id=user_id)
        return self.send_request("GET", endpoint, expected_status=expected_status)

    def delete_user(self, user_id, expected_status=204):
        """
        Удаление пользователя.
        """
        endpoint = DELETE_USER_ENDPOINT.format(user_id=user_id)
        return self.send_request("DELETE", endpoint, expected_status=expected_status)