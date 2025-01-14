import allure
import pytest
from methods.courier_methods import CourierMethods

class TestLoginCourier:

    # тест 1. успешная авторизация  курьера
    @allure.title("успешная авторизация  курьера")
    def test_login_courier(self):
        login_data = {
            "login": "sashaA",
            "password": "1234"
        }

        login_response = CourierMethods().login_courier({
            "login": "sashaA",
            "password": "1234"
        })

        assert login_response.status_code == 200, f"Ошибка логина: {login_response.json()}"
        response_json = login_response.json()
        assert "id" in response_json, "В ответе отсутствует поле 'id'"
        assert isinstance(response_json["id"], int), "Поле 'id' должно быть числом"

    # тест 2. авторизация невозможна, если ввести не все обязательные значения
    @allure.title("провальная авторизация курьера, если не ввести одно из обязательных значений")
    @pytest.mark.parametrize("missing_field, expected_message", [
        ("login", "Недостаточно данных для входа"),
        ("password", "Недостаточно данных для входа")
    ])
    def test_field_login_courier(self, missing_field, expected_message):
        base_payload = {
            "login": "sashaA",
            "password": "1234"
        }

        payload = base_payload.copy()
        payload[missing_field] = ""

        login_response = CourierMethods().login_courier(payload)

        assert login_response.status_code == 400
        assert login_response.json().get("message") == expected_message

    # тест 3. авторизация невозможна, если ввести некорректный логин или пароль
    @allure.title("провальная авторизация курьера, если указан не тот логин или пароль")
    @pytest.mark.parametrize("field_to_change, wrong_value, expected_message", [
            ("login", "wrongLogin", "Учетная запись не найдена"),
            ("password", "wrongPassword", "Учетная запись не найдена")
        ])
    def test_invalid_login_or_password(self, field_to_change, wrong_value, expected_message):
        base_payload = {
                "login": "sashaA",
                "password": "1234"
        }

        payload = base_payload.copy()
        payload[field_to_change] = wrong_value

        login_response = CourierMethods().login_courier(payload)

        assert login_response.status_code == 404
        assert login_response.json().get("message") == expected_message

    # тест 4. авторизация невозможна, если ввести несуществующие в базе данные
    @allure.title("провальная авторизация курьера, если указать нереальные данные для входа")

    def test_unreal_login (self):
        base_payload = {
                "login": "NOTsashaA",
                "password": "12not34"
            }
        login_response = CourierMethods().login_courier(base_payload)

        assert login_response.status_code == 404
        assert login_response.json().get("message") == "Учетная запись не найдена"





