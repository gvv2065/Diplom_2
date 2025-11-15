import requests 
from data import Url
from models.models import UserCreateRequest, UserLoginRequest, OrderRequest
import json
import allure

class Api:
    
    @staticmethod
    @allure.step("api: создание пользователя")
    def create_user(user: UserCreateRequest) -> requests.Response:
        response = requests.post(Url.REGISTER, data=user.__dict__)
        return response
    
    @staticmethod
    @allure.step("api: вход пользователя")
    def login_user(user: UserLoginRequest) -> requests.Response:
        response = requests.post(Url.LOGIN, data=user.__dict__)
        return response
    
    @staticmethod
    @allure.step("api: создание заказа")
    def create_order(order: OrderRequest, accessToken: str) -> requests.Response:
        if (accessToken is None):
            response = requests.post(Url.ORDERS, 
                data=json.dumps(order.__dict__),
                headers={"Content-Type": "application/json"})
        else:
            response = requests.post(Url.ORDERS, 
                data=json.dumps(order.__dict__),
                headers={"Authorization": f"{accessToken}", 
                         "Content-Type": "application/json"})
        
        return response
