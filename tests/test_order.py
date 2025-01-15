import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import requests
import pytest
import allure
from urls import CREATE_ORDER_URL, BASE_URL

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

    response = requests.post(f'{BASE_URL}{CREATE_ORDER_URL}')
    assert response.status_code == 201

    response_json = response.json()
    assert "track" in response_json