import requests 
from data import Url
from models.models import UserCreateRequest
import json
import allure

class Api:
    
    @staticmethod
    @allure.step("api: создание пользователя")
    def create_user(courier: UserCreateRequest) -> requests.Response:
        response = requests.post(Url.REGISTER, data=courier.__dict__)
        return response
