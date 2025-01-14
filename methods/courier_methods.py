import requests
import allure

BASE_URL = 'https://qa-scooter.praktikum-services.ru/api/v1'
CREATE_COURIER = '/courier'
LOGIN_COURIER = '/courier/login'

class CourierMethods:
    @allure.step('Вызов метода POST для создания курьера')
    def create_courier(self, payload):
        return requests.post(f'{BASE_URL}{CREATE_COURIER}', json=payload)

    @allure.step('Вызов метода POST для авторизации курьера')
    def login_courier(self, payload):
        return requests.post(f'{BASE_URL}{LOGIN_COURIER}', json=payload)
