import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import requests
import allure
from urls import BASE_URL, CREATE_ORDER_URL

@allure.title("В тело ответа возвращается список заказов")
def test_get_orders_list():
    response = requests.get(f'{BASE_URL}{CREATE_ORDER_URL}?courierId=444234')
    assert response.status_code == 200

    response_json = response.json()
    assert "orders" in response_json

    assert isinstance(response_json["orders"], list)