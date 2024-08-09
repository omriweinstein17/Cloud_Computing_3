# from books import books_array
# import connectionController
# from assertions import *

# # Test 1
# def test_post_books():  
#     # POST /books request for book1
#     response1 = connectionController.http_post("books", books_array[0])
#     assert_status_code(response1, [201])
#     response2 = connectionController.http_post("books", books_array[1])
#     assert_status_code(response2, [201])
#     response3 = connectionController.http_post("books", books_array[2])
#     assert_status_code(response3, [201])
#     assert_valid_post_response(response1, response2, response3)

# # Test 2
# def test_get_book_by_id():
#     # add id to string in the response
#     response = connectionController.http_get(f"books/{books_id_array[0]}")
#     assert_status_code(response, [200])
#     assert_ret_value(response, "authors", "Mark Twain")

# # Test 3
# def test_get_books():
#     response = connectionController.http_get("books")
#     assert_status_code(response, [200])
#     assert_length_and_types_of_array(response, 3)

# # Test 4 
# def test_post_books_with_invalid_ISBN():
#     response = connectionController.http_post("books", books_array[3])
#     assert_status_code(response, [400,500])
    
# # Test 5
# def test_delete_books():
#     response = connectionController.http_delete(f"books/{books_id_array[1]}")
#     assert_status_code(response, [200])

# # Test 6
# def test_get_deleted_book():
#     response = connectionController.http_get(f"books/{books_id_array[1]}")
#     assert_status_code(response, [404])

# # Test 7
# def test_post_books_with_invalid_genre():
#     response = connectionController.http_post("books", books_array[4])
#     assert_status_code(response, [422])

# ----- NIR TEST ------ 

import requests

BASE_URL = "http://localhost:5001/books"

book6 = {
    "title": "The Adventures of Tom Sawyer",
    "ISBN": "9780195810400",
    "genre": "Fiction"
}

book7 = {
    "title": "I, Robot",
    "ISBN": "9780553294385",
    "genre": "Science Fiction"
}

book8 = {
    "title": "Second Foundation",
    "ISBN": "9780553293364",
    "genre": "Science Fiction"
}

books_data = []


def test_post_books():
    books = [book6, book7, book8]
    for book in books:
        res = requests.post(BASE_URL, json=book)
        assert res.status_code == 201
        res_data = res.json()
        assert "ID" in res_data
        books_data.append(res_data)
        books_data_tuples = [frozenset(book.items()) for book in books_data]
    assert len(set(books_data_tuples)) == 3


def test_get_query():
    res = requests.get(f"{BASE_URL}?authors=Isaac Asimov")
    assert res.status_code == 200
    assert len(res.json()) == 2


def test_delete_book():
    res = requests.delete(f"{BASE_URL}/{books_data[0]['ID']}")
    assert res.status_code == 200


def test_post_book():
    book = {
        "title": "The Art of Loving",
        "ISBN": "9780062138927",
        "genre": "Science"
    }
    res = requests.post(BASE_URL, json=book)
    assert res.status_code == 201



def test_get_new_book_query():
    res = requests.get(f"{BASE_URL}?genre=Science")
    assert res.status_code == 200
    res_data = res.json()
    assert res_data[0]["title"] == "The Art of Loving"

