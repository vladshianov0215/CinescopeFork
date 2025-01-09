from Modul_4.Cinescope.api.auth_api import AuthAPI
# from Modul_4.Cinescope.api.user_api import UserAPI

class ApiManager:
    """
    Класс для управления API-классами с единой HTTP-сессией.
    """
    def __init__(self, session):
        self.session = session
        self.auth_api = AuthAPI(session)
        # self.user_api = UserAPI(session)