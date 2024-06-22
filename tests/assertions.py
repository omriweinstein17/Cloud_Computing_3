import sys
import requests
import connectionController
books_id_array = []

def assert_status_code(response: requests.Response, status_code: int):
    assert response.status_code == status_code


def assert_ret_value(response: requests.Response, field: str, returned_value: any):
    assert response.json()[field] == returned_value

def assert_valid_post_response(response1: requests.Response, response2: requests.Response, response3: requests.Response):
    id1, id2, id3 = response1.json()['ID'], response2.json()['ID'], response3.json()['ID']
    assert isinstance(id1, str) and isinstance(id2, str) and isinstance(id3, str)
    assert id1 != id2 
    assert id1 != id3
    assert id2 != id3
    books_id_array.append(id1)
    books_id_array.append(id2)
    books_id_array.append(id3)

def assert_valid_added_resource(response: requests.Response):
    assert response.status_code == 201
    # should be positive ID
    VALID_RETURNED_RESOURCE_ID = 0
    print("print(response.json()) > 0? response.json() =")
    print(response.json())
    sys.stdout.flush()
    assert response.json() > VALID_RETURNED_RESOURCE_ID


def assert_not_existed_meal(meal_identifier: any) -> None:
    response = connectionController.http_get(f"meals/{meal_identifier}")
    assert_status_code(response, error_code=404)
    assert_ret_value(response, returned_value=-5)

def assert_length_of_array(response: requests.Response, length: int):
    assert len(response.json()) == length


