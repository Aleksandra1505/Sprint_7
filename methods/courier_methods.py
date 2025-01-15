import requests
import allure
from urls import BASE_URL, CREATE_COURIER, LOGIN_COURIER


class CourierMethods:

    @allure.step('Вызов метода POST для создания курьера')
    def create_courier(self, payload):
        return requests.post(f'{BASE_URL}{CREATE_COURIER}', json=payload)

    @allure.step('Вызов метода POST для авторизации курьера')
    def login_courier(self, payload):
        return requests.post(f'{BASE_URL}{LOGIN_COURIER}', json=payload)

    @allure.step('Удалить курьера')
    def delete_courier(self, courier_id):
        return requests.delete(f'{BASE_URL}/courier/{courier_id}')

