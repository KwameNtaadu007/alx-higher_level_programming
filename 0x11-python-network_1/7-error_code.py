#!/usr/bin/python3
"""Sends a request to a given URL and displays the response body.

Python script that takes in a URL,
sends a request to the URL and displays the body of the response.
"""

import sys
import requests

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <URL>")
        sys.exit(1)

    url = sys.argv[1]

    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for 4XX/5XX status codes

        x_request_id = response.headers.get("X-Request-Id")
        if x_request_id:
            print(f"X-Request-Id: {x_request_id}")
        else:
            print("X-Request-Id not found in the response headers.")
    except requests.RequestException as e:
        print(f"Request failed: {e}")

