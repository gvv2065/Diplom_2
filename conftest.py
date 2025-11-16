import pytest

from api.Api import Api
from asserts.common_asserts import assert_response
from data import User
from helper import generate_user_create_request
from models.models import UserCreateRequest

@pytest.fixture(scope="function")
def generated_user():
    user_request = generate_user_create_request()
    response = Api.create_user(user_request)
    assert_response(response, 200)
    assert response.json().get("success") is True
    assert response.json().get("user").get("name") == user_request.name
    assert response.json().get("user").get("email") == user_request.email
    yield user_request
