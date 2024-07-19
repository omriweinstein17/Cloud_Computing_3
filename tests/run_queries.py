import requests
import json
from books import books_array
import connectionController

def post_books():
    try:
        response1 = connectionController.http_post("books", books_array[0])
        response1.raise_for_status()  # Raise an HTTPError on bad status
        response2 = connectionController.http_post("books", books_array[1])
        response2.raise_for_status()  # Raise an HTTPError on bad status
        response3 = connectionController.http_post("books", books_array[2])
        response3.raise_for_status()  # Raise an HTTPError on bad status
        response4 = connectionController.http_post("books", books_array[5])
        response4.raise_for_status()  # Raise an HTTPError on bad status
        response5 = connectionController.http_post("books", books_array[6])
        response5.raise_for_status()  # Raise an HTTPError on bad status
        response6 = connectionController.http_post("books", books_array[7])
        response6.raise_for_status()  # Raise an HTTPError on bad status
    except requests.exceptions.RequestException as e:
        error_message = f"Error with post one of the books: {e}"
        print(error_message)  # Print the error message


# Function to read queries from the file
def read_queries(file_path):
    with open(file_path, 'r') as file:
        queries = file.readlines()
    return [query.strip() for query in queries]

# Function to make HTTP GET requests with the queries
def make_requests(queries):
    responses = []
    for query in queries:
        try:
            response = connectionController.http_get(f"books{query}")
            response.raise_for_status()  # Raise an HTTPError on bad status
            responses.append(response.text)
        except requests.exceptions.RequestException as e:
            responses.append(f"error {response.status_code}")
    
    return responses

# Function to save responses to a file
def save_responses(file_path, queries, responses):
    with open(file_path, 'w') as file:
        for i in range(len(responses)):
            file.write(f"query: {queries[i]}\n")
            file.write(f"response: {json.dumps(json.loads(responses[i]))}" + "\n")

# Main function to read queries, make requests, and save responses
def main():
    post_books()
    queries_file = '../query.txt'
    responses_file = 'response.txt'
    queries = read_queries(queries_file)
    responses = make_requests(queries)
    save_responses(responses_file, queries, responses)

if __name__ == "__main__":
    main()