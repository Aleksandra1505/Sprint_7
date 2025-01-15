import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import allure
import pytest
from methods.courier_methods import CourierMethods
from helpers import generate_login_password_name
from tests.constants import DUPLICATE_LOGIN_MESSAGE

class TestCreateCourier:

    # тест 1. успешное создание курьера
    @allure.title("Успешное создание курьера")
    def test_create_courier(self):
        payload = generate_login_password_name()
        courier_methods = CourierMethods()

        # создаю курьера
        response = courier_methods.create_courier(payload)
        assert response.status_code == 201
        assert response.json() == {"ok": True}

        # получили id нового курьера
        response_login = courier_methods.login_courier(payload)
        assert response_login.status_code == 200
        courier_id = response_login.json().get("id")
        assert courier_id is not None

        # удаляю курьера после теста
        response_delete = courier_methods.delete_courier(courier_id)
        assert response_delete.status_code == 200
        assert response_delete.json() == {"ok": True}

    # тест 2. нельзя создать 2 одинаковых курьеров
    @allure.title("Нельзя создать двух одинаковых курьеров")
    def test_create_duplicate_courier(self):
        payload = generate_login_password_name()

        response_1 = CourierMethods().create_courier(payload)
        assert response_1.status_code == 201
        assert response_1.json() == {"ok": True}

        # Пытаемся создать второго курьера с тем же логином
        response_2 = CourierMethods().create_courier(payload)
        assert response_2.status_code == 409
        assert response_2.json().get("message") == DUPLICATE_LOGIN_MESSAGE

    # тест 3. нельзя создать курьера без заполнения какого либо обязательного поля
    @allure.title("Ошибка при отсутствии обязательных полей")
    @pytest.mark.parametrize("missing_field, expected_message", [
        ("login", "Недостаточно данных для создания учетной записи"),
        ("password", "Недостаточно данных для создания учетной записи")
    ])
    def test_create_courier_missing_field(self, missing_field, expected_message):
        payload = generate_login_password_name()
        payload.pop(missing_field)

        response = CourierMethods().create_courier(payload)
        assert response.status_code == 400
        assert response.json().get("message") == expected_message