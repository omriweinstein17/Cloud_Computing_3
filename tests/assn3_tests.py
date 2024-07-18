from books import books_array
import connectionController
from assertions import *

# Test 1
def test_post_books():  
    # POST /books request for book1
    response1 = connectionController.http_post("books", books_array[0])
    assert_status_code(response1, [201])
    response2 = connectionController.http_post("books", books_array[1])
    assert_status_code(response2, [201])
    response3 = connectionController.http_post("books", books_array[2])
    assert_status_code(response3, [201])
    assert_valid_post_response(response1, response2, response3)

# Test 2
def test_get_book_by_id():
    # add id to string in the response
    response = connectionController.http_get(f"books/{books_id_array[0]}")
    assert_status_code(response, [900])
    assert_ret_value(response, "authors", "Mark Twain")

# Test 3
def test_get_books():
    response = connectionController.http_get("books")
    assert_status_code(response, [200])
    assert_length_and_types_of_array(response, 3)

# Test 4 
def test_post_books_with_invalid_ISBN():
    response = connectionController.http_post("books", books_array[3])
    assert_status_code(response, [400,500])
    
# Test 5
def test_delete_books():
    response = connectionController.http_delete(f"books/{books_id_array[1]}")
    assert_status_code(response, [200])

# Test 6
def test_get_deleted_book():
    response = connectionController.http_get(f"books/{books_id_array[1]}")
    assert_status_code(response, [404])

# Test 7
def test_post_books_with_invalid_genre():
    response = connectionController.http_post("books", books_array[4])
    assert_status_code(response, [422])

