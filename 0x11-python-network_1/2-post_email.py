#!/usr/bin/python3
"""This script takes in a URL and an email,
sends a POST request to the passed
URL with the email as a parameter, and
displays the body of the response (decoded in utf-8)
"""

import sys
import urllib.request
from urllib.error import URLError, HTTPError

def get_x_request_id(url):
    try:
        request = urllib.request.Request(url)
        with urllib.request.urlopen(request) as response:
            headers = dict(response.headers)
            return headers.get("X-Request-Id")
    except HTTPError as e:
        print(f"HTTP Error: {e.code} - {e.reason}")
    except URLError as e:
        print(f"URL Error: {e.reason}")
    except Exception as e:
        print(f"An error occurred: {e}")
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

