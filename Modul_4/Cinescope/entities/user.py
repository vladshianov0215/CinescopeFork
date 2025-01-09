
from Modul_4.Cinescope.entities.roles import Role

class User:
    def __init__(self, username, password, api_manager, roles):
        self.username = username
        self.password = password
        self.api_manager = api_manager
        self.roles = [Role(role) for role in roles]

    @property
    def creds(self):
        """
        Возвращает учетные данные пользователя.
        """
        return {"email": self.username, "password": self.password}
