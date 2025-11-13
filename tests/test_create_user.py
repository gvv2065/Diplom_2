import pytest
import allure

from api.Api import Api
from helper import generate_user_create_request
from asserts.common_asserts import assert_response, assert_response_200

@allure.feature("Создание пользователя")
class TestCreateUser:
    @allure.title("Пользователь успешно создается")
    def test_create_user(self):
        response = Api.create_user(generate_user_create_request())
        assert_response(response, 200)
    