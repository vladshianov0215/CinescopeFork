
class MoviesAPI:
    """
    Класс для работы с Movies API.
    """
    def __init__(self, requester):
        """
        Инициализация MoviesAPI.
        :param requester: Экземпляр CustomRequester.
        """
        self.requester = requester

    def get_movies(self, params=None):
        """
        Получение списка фильмов.
        :param params: Параметры фильтрации.
        :return: Ответ от API.
        """
        return self.requester.send_request("GET", "/movies", params=params)

    def get_movie(self, movie_id, expected_status=200):
        """
        Получение информации о конкретном фильме.
        :param movie_id: ID фильма.
        :param expected_status: Ожидаемый статус-код.
        :return: Ответ от API.
        """
        return self.requester.send_request(
            method="GET",
            endpoint=f"/movies/{movie_id}",
            expected_status=expected_status
        )

    def create_movie(self, data, headers):
        """
        Создание нового фильма.
        :param data: Данные фильма.
        :param headers: Заголовки запроса.
        :return: Ответ от API.
        """
        print(f"🔍 Отправка запроса на {self.requester.base_url}/movies с данными {data}")
        return self.requester.send_request(
            method="POST",
            endpoint="/movies",
            data=data,
            headers=headers,
            expected_status=[201, 403]  # Ожидаем 403 для ролей без доступа
        )

    def delete_movie(self, movie_id, token):
        """
        Удаление фильма.
        :param movie_id: ID фильма.
        :param token: Токен авторизации.
        :return: Ответ от API.
        """
        headers = {"Authorization": f"Bearer {token}"}
        return self.requester.send_request("DELETE", f"/movies/{movie_id}", headers=headers)