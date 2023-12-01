#!/usr/bin/python3
"""This Script takes in a URL, sends a request to the URL and
displays the value of the X-Request-Id variable found
in the header of the response.
"""

import sys
import urllib.request

def get_x_request_id(url):
    try:
        request = urllib.request.Request(url)
        with urllib.request.urlopen(request) as response:
            headers = dict(response.headers)
            return headers.get("X-Request-Id")
    except Exception as e:
        print(f"Error: {e}")
        return None

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <URL>")
        sys.exit(1)

    url = sys.argv[1]
    x_request_id = get_x_request_id(url)
    if x_request_id:
        print(f"X-Request-Id: {x_request_id}")
    else:
        print("X-Request-Id not found or an error occurred.")
