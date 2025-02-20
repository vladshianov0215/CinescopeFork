
import datetime
import pytest
import requests
from sqlalchemy.orm.session import Session
from Modul_4.Cinescope.constants import BASE_URL, HEADERS, REGISTER_ENDPOINT,  LOGIN_ENDPOINT
from Modul_4.Cinescope.custom_requester.custom_requester import CustomRequester
from Modul_4.Cinescope.api.api_manager import  ApiManager
from Modul_4.Cinescope.db_requester.models import UserDBModel
from Modul_4.Cinescope.enums.roles import Roles
from Modul_4.Cinescope.models.base_models import RegisterUserResponse, TestUser

class TestAuthAPI:
    def test_register_user(self, api_manager: ApiManager, test_user: TestUser):
        """
        Тест на регистрацию пользователя.
        """
        response = api_manager.auth_api.register_user(test_user)

        register_user_response = RegisterUserResponse(**response.json())
        assert register_user_response.email ==  test_user.email, "Email не совпадает"

    def test_register_user_db_session(self, api_manager: ApiManager, test_user: TestUser, db_session: Session):
        """
        Тест на регистрацию пользователя с проверкой в базе данных.
        """
        #выполняем запрос на регистрацию нового пользователя
        response = api_manager.auth_api.register_user(test_user)
        register_user_response = RegisterUserResponse(**response.json())
        
        #Проверяем добавил ли сервис Auth нового пользователя в базу данных
        users_from_db = db_session.query(UserDBModel).filter(UserDBModel.id == register_user_response.id)

        #получили обьект из бзы данных и проверили что он действительно существует в единственном экземпляре
        assert users_from_db.count() == 1, "обьект не попал в базу данных"
        #Достаем первый и единственный обьект из списка полученных
        user_from_db = users_from_db.first()
        #можем осуществить проверку всех полей в базе данных например Email
        assert user_from_db.email == test_user.email, "Email не совпадает"


    def test_register_user_mock(self, api_manager: ApiManager, test_user: TestUser, mocker):
        # Ответ полученный из мок сервиса
        mock_response = RegisterUserResponse(  # Фиктивный ответ
                id = "id",
                email = "email@email.com",
                fullName = "fullName",
                verified = True,
                banned = False,
                roles = [Roles.SUPER_ADMIN],
                createdAt = str(datetime.datetime.now())
            )
        
        # Мокаем метод register_user в auth_api
        mocker.patch.object(
            api_manager.auth_api,  # Объект, который нужно замокать
            'register_user',       # Метод, который нужно замокать
            return_value=mock_response  # Фиктивный ответ
        )
        # Вызываем метод, который должен быть замокан
        register_user_response = api_manager.auth_api.register_user(test_user)
        # Проверяем, что ответ соответствует ожидаемому
        assert register_user_response.email == mock_response.email, "Email не совпадает"
        