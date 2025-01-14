import requests
import pytest
import allure

@pytest.mark.parametrize("color", [
    ["BLACK"],
    ["GREY"],
    ["BLACK", "GREY"],
    None
])
@allure.title("Выбор разных цветов товара при оформлении заказа")
def test_get_orders(color):
    payload = {
        "firstName": "Naruto",
        "lastName": "Uchiha",
        "address": "Konoha, 142 apt.",
        "metroStation": 4,
        "phone": "+7 800 355 35 35",
        "rentTime": 5,
        "deliveryDate": "2020-06-06",
        "comment": "Saske, come back to Konoha",
        "color": color
    }

    response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/orders',
        json=payload)
    assert response.status_code == 201

    response_json = response.json()
    assert "track" in response_json