#!/usr/bin/python3

import requests

def top_ten(subreddit):
    # Reddit API endpoint for hot posts
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    
    # Set custom User-Agent to avoid issues
    headers = {'User-Agent': 'MyRedditBot/1.0'}
    
    try:
        # Make a GET request to the Reddit API
        response = requests.get(url, headers=headers)
        
        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse the JSON response
            subreddit_data = response.json()
            
            # Extract and print the titles of the first 10 hot posts
            for post in subreddit_data['data']['children']:
                print(post['data']['title'])
        else:
            # If the subreddit is invalid, print None
            print(None)
    except Exception as e:
        print(f"Error: {e}")
        print(None)

if __name__ == '__main__':
    import sys
    
    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        subreddit = sys.argv[1]
        top_ten(subreddit)

