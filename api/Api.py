import requests 
from data import Url
from models.models import UserCreateRequest, UserLoginRequest
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
