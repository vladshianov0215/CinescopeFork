from Modul_4.Cinescope.enums.roles import Roles
from Modul_4.Cinescope.utils.data_generator import DataGenerator

class UserData:
    @staticmethod
    def generate_user_data(role=Roles.USER.value):
        """
        Генерирует данные для создания пользователя с указанной ролью.
        """
        return {
            "email": DataGenerator.generate_random_email(),
            "fullName": DataGenerator.generate_random_name(),
            "password": DataGenerator.generate_random_password(),
            "verified": True,
            "banned": False,
            "roles": [role]
        }