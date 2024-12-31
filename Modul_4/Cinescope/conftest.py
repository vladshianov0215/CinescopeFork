
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
def registered_user(requester, test_user):
    """
    Фикстура для регистрации и получения данных зарегистрированного пользователя.
    """
    # Регистрируем пользователя
    response = requester.send_request(
        method="POST",
        endpoint=REGISTER_ENDPOINT,
        data=test_user,
        expected_status=201
    )
    response_data = response.json()

    # Обновляем данные пользователя (включаем ID из ответа регистрации)
    registered_user = test_user.copy()
    registered_user["id"] = response_data["id"]

    return registered_user

@pytest.fixture(scope="session")
def requester():
    """
    Фикстура для создания экземпляра CustomRequester.
    """
    session = requests.Session()
    return CustomRequester(session=session, base_url=BASE_URL)


@pytest.fixture(scope="session")
def auth_api(requester):
    """
    Фикстура для работы с AuthAPI.
    """
    return AuthAPI(session=requester)



# @pytest.fixture(scope="session")
# def user_api(requester):
#     """
#     Фикстура для работы с UserAPI.
#     """
#     return UserAPI(session=requester)

@pytest.fixture(scope="session")
def session():
    """
    Фикстура для создания HTTP-сессии.
    """
    http_session = requests.Session()
    yield http_session
    http_session.close()


@pytest.fixture(scope="session")
def api_manager(session):
    """
    Фикстура для создания экземпляра ApiManager.
    """
    return ApiManager(session)