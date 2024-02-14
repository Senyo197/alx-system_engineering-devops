#!/usr/bin/python3
""" A function that queries the Reddit API and returns the number
    of subscribers (not active users, total subscribers)
    for a given subreddit
"""

import requests


def number_of_subscribers(subreddit):
    """
    Queries the Reddit API and returns the number of subscribers
    for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit.

    Returns:
        int: The number of subscribers for the subreddit,
             or 0 if the subreddit is invalid.
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64)\
               AppleWebKit/537.36"}

    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 404:
        return 0

    try:
        data = response.json().get("data")
        subscribers = data.get("subscribers")
        return subscribers
    except Exception as e:
        print(f"Error: {e}")
        return 0
