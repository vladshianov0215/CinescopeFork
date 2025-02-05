from Modul_4.Cinescope.enums.roles import Roles
from Modul_4.Cinescope.utils.data_generator import DataGenerator

class UserData:
    @staticmethod
    def generate_user_data(role):
        """Генерирует корректные данные пользователя с указанной ролью."""
        password = DataGenerator.generate_random_password()

        return {
            "email": DataGenerator.generate_random_email(),
            "fullName": DataGenerator.generate_random_name(),
            "password": password,  # Сохраняем пароль
            "passwordRepeat": password,  # Дублируем пароль
            "verified": True,
            "banned": False,
            "roles": [role]  # Назначаем переданную роль
        }