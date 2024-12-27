import pytest
from constants import BASE_URL

class TestBookings:
    def test_create_booking(self, auth_session, booking_data):
        # Создаём бронирование
        create_booking = auth_session.post(f"{BASE_URL}/booking", json=booking_data)
        assert create_booking.status_code == 200, "Ошибка при создании брони"

        booking_id = create_booking.json().get("bookingid")
        assert booking_id is not None, "Идентификатор брони не найден в ответе"
        assert create_booking.json()["booking"]["firstname"] == booking_data["firstname"], "Заданное имя не совпадает"
        assert create_booking.json()["booking"]["totalprice"] == booking_data["totalprice"], "Заданная стоимость не совпадает"

        # Проверяем, что бронирование можно получить по ID
        get_booking = auth_session.get(f"{BASE_URL}/booking/{booking_id}")
        assert get_booking.status_code == 200, "Бронь не найдена"
        assert get_booking.json()["lastname"] == booking_data["lastname"], "Заданная фамилия не совпадает"

        # Удаляем бронирование
        deleted_booking = auth_session.delete(f"{BASE_URL}/booking/{booking_id}")
        assert deleted_booking.status_code == 201, "Бронь не удалилась"

        # Проверяем, что бронирование больше недоступно
        get_booking = auth_session.get(f"{BASE_URL}/booking/{booking_id}")
        assert get_booking.status_code == 404, "Бронь не удалилась"

def test_update_booking_with_put(auth_session, booking_data):
    # Создаём бронирование
    create_response = auth_session.post(f"{BASE_URL}/booking", json=booking_data)
    booking_id = create_response.json().get("bookingid")
    assert booking_id is not None

    # Данные для обновления
    updated_data = {
        "firstname": "UpdatedName",
        "lastname": "UpdatedLastName",
        "totalprice": 50000,
        "depositpaid": False,
        "bookingdates": {
            "checkin": "2024-05-01",
            "checkout": "2024-05-10"
        },
        "additionalneeds": "UpdatedNeeds"
    }

    # Отправляем PUT-запрос
    update_response = auth_session.put(f"{BASE_URL}/booking/{booking_id}", json=updated_data)
    assert update_response.status_code == 200

    # Проверяем обновление
    get_response = auth_session.get(f"{BASE_URL}/booking/{booking_id}")
    assert get_response.json() == updated_data
    
def test_update_booking_with_patch(auth_session, booking_data):
    # Создаём бронирование
    create_response = auth_session.post(f"{BASE_URL}/booking", json=booking_data) # Дальше сами
    booking_id = create_response.json().get("bookingid")
    assert booking_id is not None

    # Данные для частичного обновления
    patch_data = {
        "firstname": "PatchedName",
        "additionalneeds": "NewNeeds"
    }

    # Отправляем PATCH-запрос
    patch_response = auth_session.patch(f"{BASE_URL}/booking/{booking_id}", json=patch_data)
    assert patch_response.status_code == 200

    # Проверяем, что изменения затронули только указанные поля
    get_response = auth_session.get(f"{BASE_URL}/booking/{booking_id}")
    assert get_response.json()["firstname"] == "PatchedName"
    assert get_response.json()["additionalneeds"] == "NewNeeds"
    assert get_response.json()["lastname"] == booking_data["lastname"]  # Поле не должно измениться
