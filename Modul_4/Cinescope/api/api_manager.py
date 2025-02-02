from Modul_4.Cinescope.api.auth_api import AuthAPI
from Modul_4.Cinescope.api.movies_api import MoviesAPI



class ApiManager:
    """
    Класс для управления API-классами с разными базовыми URL.
    """
    def __init__(self, auth_requester, movies_requester):
        """
        Инициализация ApiManager.
        :param auth_requester: CustomRequester для Auth API.
        :param movies_requester: CustomRequester для Movies API.
        """
        self.auth_api = AuthAPI(auth_requester)
        self.movies_api = MoviesAPI(movies_requester)

    def __getattr__(self, item):
        """
        Позволяет обращаться к API-клиентам через атрибуты.
        :param item: Название API-клиента.
        :return: Экземпляр API-клиента.
        """
        if item in self.api_clients:
            return self.api_clients[item]
        raise AttributeError(f"No API client named '{item}' in ApiManager.")