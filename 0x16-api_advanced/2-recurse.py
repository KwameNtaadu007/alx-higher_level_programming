#!/usr/bin/python3

import requests

def recurse(subreddit, hot_list=[], after=None):
    # Reddit API endpoint for hot posts
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=100&after={after}"
    
    # Set custom User-Agent to avoid issues
    headers = {'User-Agent': 'MyRedditBot/1.0'}
    
    try:
        # Make a GET request to the Reddit API
        response = requests.get(url, headers=headers)
        
        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse the JSON response
            subreddit_data = response.json()
            
            # Extract and append the titles of the current set of hot articles to the hot_list
            for post in subreddit_data['data']['children']:
                hot_list.append(post['data']['title'])
            
            # Check if there are more pages (next page marker 'after' is present)
            after = subreddit_data['data']['after']
            if after is not None:
                # Make a recursive call with the updated 'after' parameter
                return recurse(subreddit, hot_list, after)
            else:
                # If no more pages, return the final hot_list
                return hot_list
        else:
            # If the subreddit is invalid, return None
            return None
    except Exception as e:
        print(f"Error: {e}")
        return None

if __name__ == '__main__':
    import sys
    
    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        subreddit = sys.argv[1]
        result = recurse(subreddit)
        if result is not None:
            print(len(result))
        else:
            print("None")

