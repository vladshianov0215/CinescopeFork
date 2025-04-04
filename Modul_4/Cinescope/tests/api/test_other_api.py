import datetime
import pytest
import allure
import time
import random
from pytz import timezone
from sqlalchemy.orm.session import Session
from Modul_4.Cinescope.api.api_manager import ApiManager
from Modul_4.Cinescope.db_requester.models import AccountTransactionTemplate, MovieDBModel
from Modul_4.Cinescope.utils.data_generator import DataGenerator

class TestMoviesAPI:
    """
    Тесты для Movies API.
    """

    def test_get_all_movies(self, api_manager):
        """
        Тест для получения всех фильмов.
        """
        response = api_manager.movies_api.get_movies()
        assert response.status_code == 200, "Статус-код должен быть 200"
        assert "movies" in response.json(), "Ответ должен содержать ключ 'movies'"
        assert isinstance(response.json()["movies"], list), "'movies' должен быть списком"

    def test_get_movie_by_id(self, api_manager):
        """
        Тест для получения фильма по ID.
        """
        # Предположим, что фильм с ID '12345' существует
        movie_id = 50
        response = api_manager.movies_api.get_movie(movie_id)
        assert response.status_code == 200, "Статус-код должен быть 200"
        movie_data = response.json()
        assert movie_data.get("id") == movie_id, "ID фильма должен совпадать"
        assert "name" in movie_data, "Фильм должен содержать ключ 'name'"
        assert "price" in movie_data, "Фильм должен содержать ключ 'price'"

    def test_create_movie(self, api_manager, super_admin_token):
        """
        Тест для создания нового фильма.
        """
        movie_data = {
        "name": "Test Movie123",
        "price": 500,
        "description": "Описание тестового фильма",
        "location": "MSK",  # Исправлено значение location
        "published": True,
        "genreId": 1  # Исправлено значение genreId
        }
        response = api_manager.movies_api.create_movie(
            data=movie_data, 
            headers = {"Authorization": f"Bearer {super_admin_token}"}
            )
        assert response.status_code == 201, "Фильм должен успешно создаться"
        created_movie = response.json()
        assert created_movie["name"] == movie_data["name"], "Имя фильма должно совпадать"
        assert created_movie["price"] == movie_data["price"], "Цена фильма должна совпадать"

    def test_delete_movie(self, api_manager, super_admin_token):
        """
        Тест для удаления фильма.
        """
        # Задайте заранее известный ID существующего фильма
        movie_id = 54  # Убедитесь, что этот фильм существует в базе данных

        # Удаляем фильм
        delete_response = api_manager.movies_api.delete_movie(movie_id=movie_id, token=super_admin_token)
        assert delete_response.status_code == 200, "Фильм должен успешно удалиться"

        # Проверяем, что фильм действительно удалён
        get_response = api_manager.movies_api.get_movie(movie_id=movie_id, expected_status=404)
        assert get_response.status_code == 404, "Фильм не должен существовать после удаления"

    def test_create_delete_movie(self, api_manager, super_admin_token, db_session: Session):
        #как бы выглядел SQL запрос
        """SELECT id, "name", price, description, image_url, "location", published, rating, genre_id, created_at
           FROM public.movies
           WHERE name='Test Moviej1h8qss9s5';"""

        movie_name = f"Test Movie{DataGenerator.generate_random_str(10)}"
        movies_from_db = db_session.query(MovieDBModel).filter(MovieDBModel.name == movie_name)

        #проверяем что до начала тестирования фильма с таким названием нет
        assert movies_from_db.count() == 0, "В базе уже присутствует фильм с таким названием"

        movie_data = {
            "name": movie_name,
            "price": 500,
            "description": "Описание тестового фильма",
            "location": "MSK",
            "published": True,
            "genreId": 3
        }
        response = api_manager.movies_api.create_movie(
            data=movie_data, 
            headers = {"Authorization": f"Bearer {super_admin_token}"}
            )
        assert response.status_code == 201, "Фильм должен успешно создаться"
        response=response.json()

        #проверяем после вызова api_manager.movies_api.create_movie в базе появился наш фильм
        movies_from_db = db_session.query(MovieDBModel).filter(MovieDBModel.name == movie_name)
        assert movies_from_db.count() == 1, "В базе уже присутствует фильм с таким названием"
        
        movie_from_db = movies_from_db.first()
        # можете обратить внимание что в базе данных етсь поле created_at которое мы не здавали явно
        # наш сервис сам его заполнил. проверим что он заполнил его верно с погрешностью в 5 минут
        assert movie_from_db.created_at >= (datetime.datetime.now(timezone('UTC')).replace(tzinfo=None) - datetime.timedelta(minutes=5)), "Сервис выставил время создания с большой погрешностью"
                
        # Берем айди фильма который мы только что создали и  удаляем его из базы через апи
        # Удаляем фильм
        delete_response = api_manager.movies_api.delete_movie(movie_id=response["id"] , token=super_admin_token)
        assert delete_response.status_code == 200, "Фильм должен успешно удалиться"

        #проверяем что в конце тестирования фильма с таким названием действительно нет в базе
        movies_from_db = db_session.query(MovieDBModel).filter(MovieDBModel.name == movie_name)
        assert movies_from_db.count() == 0, "Фильм небыл удален из базы!"

@allure.epic("Тестирование транзакций")
@allure.feature("Тестирование транзакций между счетами")
class TestAccountTransactionTemplate:

    @allure.story("Корректность перевода денег между двумя счетами")
    @allure.description("""
    Этот тест проверяет корректность перевода денег между двумя счетами.
    Шаги:
    1. Создание двух счетов: Stan и Bob.
    2. Перевод 200 единиц от Stan к Bob.
    3. Проверка изменения балансов.
    4. Очистка тестовых данных.
    """)
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.label("qa_name", "Ivan Petrovich")
    @allure.title("Тест перевода денег между счетами 200 рублей")
    def test_accounts_transaction_template(self, db_session: Session):
        # ====================================================================== Подготовка к тесту
        with allure.step("Создание тестовых данных в базе данных: счета Stan и Bob"):
            stan = AccountTransactionTemplate(user=f"Stan_{DataGenerator.generate_random_int(10)}", balance=1000)
            bob = AccountTransactionTemplate(user=f"Bob_{DataGenerator.generate_random_int(10)}", balance=500)
            db_session.add_all([stan, bob])
            db_session.commit() 
        
        @allure.step("Функция перевода денег: transfer_money")
        @allure.description( """
            функция выполняющая транзакцию, имитация вызова функции на стороне тестируемого сервиса
            и вызывая метод transfer_money, мы какбудтобы делем запрос в api_manager.movies_api.transfer_money
            """)
        def transfer_money(session, from_account, to_account, amount):
            with allure.step(" Получаем счета"):
                from_account = session.query(AccountTransactionTemplate).filter_by(user=from_account).one()
                to_account = session.query(AccountTransactionTemplate).filter_by(user=to_account).one()

            with allure.step("Проверяем, что на счете достаточно средств"):
                if from_account.balance < amount:
                    raise ValueError("Недостаточно средств на счете")

            with allure.step("Выполняем перевод"):
                from_account.balance -= amount
                to_account.balance += amount

            with allure.step("Сохраняем изменения"):
                session.commit()

        # ====================================================================== Тест
        with allure.step("Проверяем начальные балансы"):
            assert stan.balance == 1000
            assert bob.balance == 500

        try:
            with allure.step("Выполняем перевод 200 единиц от stan к bob"):
                transfer_money(db_session, from_account=stan.user, to_account=bob.user, amount=200)

            with allure.step("Проверяем, что балансы изменились"):
                assert stan.balance == 800
                assert bob.balance == 700

        except Exception as e:
            with allure.step("ОШИБКА откаты транзакции"):
                db_session.rollback()

            pytest.fail(f"Ошибка при переводе денег: {e}")

        finally:
            with allure.step("Удаляем данные для тестирования из базы"):
                db_session.delete(stan)
                db_session.delete(bob)
                db_session.commit()

    @allure.title("Тест с перезапусками")
    @pytest.mark.flaky(reruns=3)
    def test_with_retries(delay_between_retries):
        with allure.step("Шаг 1: Проверка случайного значения"):
            result = random.choice([True, False])
            assert result, "Тест упал, потому что результат False"