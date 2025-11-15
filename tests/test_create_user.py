import pytest
import allure

from api.Api import Api
from helper import generate_user_create_request
from asserts.common_asserts import assert_response
from data import User
from models.models import UserCreateRequest

@allure.feature("Создание пользователя")
class TestCreateUser:
    @allure.title("Пользователь успешно создается")
    def test_create_user(self):
        response = Api.create_user(generate_user_create_request())
        assert_response(response, 200)
    
    @allure.title("Если пользователь существует, вернется код ответа 403")
    def test_create_existed_user(self):
        response = Api.create_user(UserCreateRequest(User.EMAIL, User.PASSWORD, "Vitaly"))
        resp = assert_response(response, 403)
        assert resp == {"message": "User already exists", "success": False}

    @allure.title("Если отсутствует одно из обязательных полей, вернется сообщение об ошибке")
    @pytest.mark.parametrize("email,password,name", [
        ("", User.PASSWORD, "Vitaly"),
        (User.EMAIL, "", "Vitaly"),
        (User.EMAIL, User.PASSWORD, ""),
    ])
    def test_create_user_missing_required_field(self, email, password, name):
        request = UserCreateRequest(email, password, name)
        response = Api.create_user(request)
        resp = assert_response(response, 403)
        assert resp == {"message": "Email, password and name are required fields", "success": False}
        