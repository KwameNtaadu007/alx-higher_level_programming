#!/usr/bin/python3
"""Python script that takes in a URL,
sends a request to the URL and displays the body
of the response (decoded in utf-8).
"""

import sys
import urllib.error
import urllib.request

def fetch_url_body(url):
    try:
        request = urllib.request.Request(url)
        with urllib.request.urlopen(request) as response:
            return response.read().decode("utf-8")
    except urllib.error.HTTPError as e:
        print(f"HTTP Error: {e.code} - {e.reason}")
    except urllib.error.URLError as e:
        print(f"URL Error: {e.reason}")
    except Exception as e:
        print(f"An error occurred: {e}")
    return None

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <URL>")
        sys.exit(1)

    url = sys.argv[1]
    response_body = fetch_url_body(url)
    if response_body:
        print(response_body)
    else:
        print("Error retrieving the URL body.")

