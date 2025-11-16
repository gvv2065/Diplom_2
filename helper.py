from datetime import datetime, timedelta
import random
import string
from models.models import UserCreateRequest
from dataclasses import dataclass, replace
from faker import Faker

def generate_user_create_request() -> UserCreateRequest: 
    faker = Faker()
    email = faker.email() + "gvv"
    password = generate_random_string(10)
    name = faker.name()
    return UserCreateRequest(email, password, name)

def generate_random_string(length):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(length))
        return random_string