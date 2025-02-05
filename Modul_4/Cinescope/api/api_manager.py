from Modul_4.Cinescope.api.auth_api import AuthAPI
from Modul_4.Cinescope.api.movies_api import MoviesAPI
from Modul_4.Cinescope.custom_requester.custom_requester import CustomRequester


class ApiManager:
    def __init__(self, auth_requester: CustomRequester, movies_requester: CustomRequester):
        self.auth_api = AuthAPI(auth_requester)  # ✅ Передаём CustomRequester
        self.movies_api = MoviesAPI(movies_requester)  # ✅ Передаём CustomRequeste