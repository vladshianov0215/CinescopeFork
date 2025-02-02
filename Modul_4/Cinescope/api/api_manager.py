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
