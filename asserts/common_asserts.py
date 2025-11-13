def assert_response_200(response):
    return assert_response(response, 200)
    
def assert_response(response, status_code):
    assert response.status_code == status_code
    return response.json()