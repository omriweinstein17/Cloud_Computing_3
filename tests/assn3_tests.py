# The tests to execute
# There are 7 tests to be executed in pytest against your image:
# 1. Execute three POST /books requests supplying the details of book1, book2, and book3 (see slide “Books”). The test is successful* if (i) all 3
# requests return unique IDs (none of the IDs are the same), and (ii) the
# return status code from each POST request is 201.
# 2. Execute a GET books/<-ID> request, using the ID of book1 Adventures of
# Huckleberry Finn. The test is successful if (i) the authors field equals “Mark
# Twain” and (ii) the return status code from the request is 200.
# 3. Execute a GET /books request. The test is successful if (i) the returned JSON object has 3 embedded JSON objects (books), and (ii) the return
# status code from the GET request is 200.
# * “The test is successful” means that your pytest needs to test for these
# conditions.
# The tests to execute
# 4. Execute a POST /books request supplying the details of book4. The test is
# successful if the return status code is 500 (since Google Books API will
# return an error because the ISBN number is not correct).
# 5. Perform a DELETE /books request, using the ID of book2 The Best of Isaac
# Asimov. The test is successful if the return status code is 200.
# 6. Perform a GET books/<-ID> request, using the ID of book2. The test is
# successful if the return status code is 404.
# 7. Execute a POST /books request supplying the details of book5. The test is
# successful if the return status code is or 422 (the genre is not an
# acceptable one). 

import requests
import json
import pytest
import random
import string

# Test 1
def test_post_books():
    # Book 1
    book1 = {
        "title": "Adventures of Huckleberry Finn",
        "authors": "Mark Twain",
        "publishedDate": "1884-12-10",
        "ISBN": "9780199536559",
        "genre": "Adventure"
    }
    # Book 2
    book2 = {
        "title": "The Best of Isaac Asimov",
        "authors": "Isaac Asimov",
        "publishedDate": "1973-01-01",
        "ISBN": "9780385420785",
        "genre": "Science Fiction"
    }
    # Book 3
    book3 = {
        "title": "The Great Gatsby",
        "authors": "F. Scott Fitzgerald",
        "publishedDate": "1925-04-10",
        "ISBN": "9780743273565",
        "genre": "Fiction"
    }

    # POST /books request for book1
    response1 = requests.post("http://localhost:5001/books", json=book1)
    
    # POST /books request for book2
    response2 = requests.post("http://localhost:5001/books", json=book2)

    # 
    response3 = requests.post("http://localhost:5001/books", json=book3)