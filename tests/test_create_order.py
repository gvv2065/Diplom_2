import allure

from api.Api import Api
from asserts.common_asserts import assert_response
from data import User, DEFAULT_INGRDIENTS_IDS
from models.models import UserLoginRequest, OrderRequest

@allure.feature("Создание заказа")
class TestCreateOrder:
    @allure.title("Создание заказа с авторизацией")
    def test_create_order_when_logged_in(self):
        userResponse = Api.login_user(UserLoginRequest(User.EMAIL, User.PASSWORD))
        response = Api.create_order(OrderRequest(DEFAULT_INGRDIENTS_IDS),
            userResponse.json().get("accessToken"))
        resp = assert_response(response, 200)
        assert resp.get("order").get("number") is not None
        assert resp.get("success") is True
        assert resp.get("order").get("owner").get("name") == "Vit"
        
    @allure.title("Создание заказа без авторизации с ингредиентами")
    def test_create_order_without_login(self):
        response = Api.create_order(OrderRequest(DEFAULT_INGRDIENTS_IDS), None)
        resp = assert_response(response, 200)
        assert resp.get("success") is True
        assert resp.get("order").get("number") is not None
        assert resp.get("name") is not None
        
    @allure.title("Создание заказа без ингредиентов")
    def test_create_order_without_ingredients(self):
        response = Api.create_order(OrderRequest([]), None)
        resp = assert_response(response, 400)
        assert resp.get("success") is False
        assert resp.get("message") == "Ingredient ids must be provided"
        
    @allure.title("Создание заказа c неверным хешем ингредиентов")
    def test_create_order_with_wrong_ingredient_hash(self):
        response = Api.create_order(OrderRequest(["unknownhash"]), None)
        assert response.status_code == 500
