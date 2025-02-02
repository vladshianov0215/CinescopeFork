
from faker import Faker
import pytest
import requests

from Modul_4.Cinescope.api.movies_api import MoviesAPI
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
    movies_requester = CustomRequester(session, base_url="https://api.dev-cinescope.coconutqa.ru")  # Добавляем второй аргумент
    yield ApiManager(session, movies_requester)



# @pytest.fixture(scope="session")
# def api_manager(session):
#     """
#     Фикстура для создания ApiManager с разными базовыми URL.
#     """
#     auth_requester = CustomRequester(
#         session=session,
#         base_url="https://auth.dev-cinescope.coconutqa.ru"
#     )
#     movies_requester = CustomRequester(
#         session=session,
#         base_url="https://api.dev-cinescope.coconutqa.ru"
#     )
#     return ApiManager(auth_requester, movies_requester)


@pytest.fixture
def movie_data():
    """
    Генерация данных для создания фильма.
    """
    return {
        "name": "Test Movie",
        "price": 500,
        "description": "Описание тестового фильма",
        "location": "MSK",  # Исправлено значение location
        "published": True,
        "genreId": 1  # Исправлено значение genreId
    }

@pytest.fixture(scope="session")
def super_admin_token(api_manager):
    """
    Получение токена для авторизации супер-админа.
    """
    login_data = {
        "email": "test-admin@mail.com",  # Убедитесь, что email супер-админа корректен
        "password": "KcLMmxkJMjBD1"      # Убедитесь, что пароль супер-админа корректен
    }
    response = api_manager.auth_api.login_user(login_data)
    assert response.status_code == 200, "Не удалось авторизоваться как супер-админ"
    return response.json()["accessToken"]

@pytest.fixture(scope="session")
def movies_api(requester):
    """
    Фикстура для MoviesAPI.
    """
    movies_base_url = "https://api.dev-cinescope.coconutqa.ru"
    return MoviesAPI(requester(movies_base_url), base_url=movies_base_url)

