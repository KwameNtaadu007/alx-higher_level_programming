#!/usr/bin/python3
"""
Python script that fetches https://alx-intranet.hbtn.io/status
"""

import requests

def fetch_url(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for 4XX/5XX status codes
        return response.text
    except requests.RequestException as e:
        print(f"Request failed: {e}")
    return None

if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"
    content = fetch_url(url)
    if content:
        print("Body response:")
        print(f"\t- type: {type(content)}")
        print(f"\t- content: {content}")
    else:
        print("Failed to fetch the URL content.")

