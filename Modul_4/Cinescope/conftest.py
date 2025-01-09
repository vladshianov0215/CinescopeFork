
from faker import Faker
import pytest
import requests
from Modul_4.Cinescope.constants import BASE_URL, REGISTER_ENDPOINT, LOGIN_ENDPOINT
from Modul_4.Cinescope. custom_requester.custom_requester import CustomRequester
from Modul_4.Cinescope.utils.data_generator import DataGenerator
from Modul_4.Cinescope.api.auth_api import AuthAPI
# from Modul_4.Cinescope.api.user_api import UserAPI
from Modul_4.Cinescope.api.api_manager import ApiManager

faker = Faker()

@pytest.fixture(scope="session")
def test_user():
    """
    Генерация случайного пользователя для тестов.
    """
    random_email = DataGenerator.generate_random_email()
    random_name = DataGenerator.generate_random_name()
    random_password = DataGenerator.generate_random_password()

    return {
        "email": random_email,
        "fullName": random_name,
        "password": random_password,
        "passwordRepeat": random_password,  # Убедимся, что password и passwordRepeat совпадают
        "roles": ["USER"]
    }
@pytest.fixture(scope="session")
def registered_user(api_manager, test_user):
    """
    Фикстура для регистрации пользователя через auth_api.
    """
    response = api_manager.auth_api.register_user(test_user)
    response_data = response.json()
    test_user["id"] = response_data["id"]
    return test_user





@pytest.fixture(scope="session")
def api_manager():
    """
    Фикстура для создания экземпляра ApiManager.
    """
    session = requests.Session()
    yield ApiManager(session)
    session.close()


