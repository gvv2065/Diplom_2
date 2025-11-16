import pytest
import allure

from api.Api import Api
from asserts.common_asserts import assert_response
from data import User
from models.models import UserLoginRequest

@allure.feature("Логин пользователя")
class TestLoginUser:
    @allure.title("Вход под существующем пользователем")
    def test_login_user_success(self):
        response = Api.login_user(UserLoginRequest(User.EMAIL, User.PASSWORD))
        resp = assert_response(response, 200)
        assert "accessToken" in resp
        assert "refreshToken" in resp
        assert resp.get("user") == {"email": User.EMAIL, "name": "Vit"}
        
    @allure.title("Вход под неправильным паролем или логином пользователем возвращает 401")
    @pytest.mark.parametrize("email, password", [
        ("notExistedUserLoginGvv", "doesntMatter"),
        (User.EMAIL, "wrongpassword"),
    ])
    def test_login_with_wrong_auth(self, email, password):
        response = Api.login_user(UserLoginRequest(email, password))
        resp = assert_response(response, 401)
        assert resp == {"message": "email or password are incorrect", "success": False}
