import requests
import allure


@allure.title("В тело ответа возвращается список заказов")
def test_get_orders_list():
    response = requests.get('https://qa-scooter.praktikum-services.ru/api/v1/orders?courierId=444234')
    assert response.status_code == 200

    response_json = response.json()
    assert "orders" in response_json

    assert isinstance(response_json["orders"], list)