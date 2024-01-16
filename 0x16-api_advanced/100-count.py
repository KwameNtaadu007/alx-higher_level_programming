#!/usr/bin/python3

import requests

def count_words(subreddit, word_list, after=None, word_counts={}):
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
            
            # Extract and count the occurrences of keywords in the titles
            for post in subreddit_data['data']['children']:
                title = post['data']['title'].lower()
                for keyword in word_list:
                    keyword_lower = keyword.lower()
                    if keyword_lower in title:
                        word_counts[keyword_lower] = word_counts.get(keyword_lower, 0) + title.count(keyword_lower)
            
            # Check if there are more pages (next page marker 'after' is present)
            after = subreddit_data['data']['after']
            if after is not None:
                # Make a recursive call with the updated 'after' parameter
                return count_words(subreddit, word_list, after, word_counts)
            else:
                # If no more pages, print the word counts in the required format
                print_results(word_counts)
        else:
            # If the subreddit is invalid, print nothing
            return
    except Exception as e:
        print(f"Error: {e}")
        return

def print_results(word_counts):
    # Sort the word counts in descending order by count and alphabetically by keyword
    sorted_word_counts = sorted(word_counts.items(), key=lambda x: (-x[1], x[0]))
    
    # Print the results
    for keyword, count in sorted_word_counts:
        print(f"{keyword}: {count}")

if __name__ == '__main__':
    import sys
    
    if len(sys.argv) < 3:
        print("Usage: {} <subreddit> <list of keywords>".format(sys.argv[0]))
        print("Ex: {} programming 'python java javascript'".format(sys.argv[0]))
    else:
        subreddit = sys.argv[1]
        keywords = sys.argv[2].split()
        count_words(subreddit, keywords)

