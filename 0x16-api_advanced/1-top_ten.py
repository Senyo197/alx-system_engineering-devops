#!/usr/bin/python3

""" A function that queries the Reddit API and prints the titles of the first
    10 hot posts listed for a given subreddit
"""


import requests


def top_ten(subreddit):
    """
    Queries the Reddit API and prints the titles of the first
    10 hot posts listed for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit to query.

    Returns:
        None: If the subreddit is not found or if there are no posts available.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) \
               AppleWebKit/537.36"}
    params = {"limit": 10}
    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 404:
        print("None")
        return

    data = response.json().get("data", {}).get("children", [])
    if not data:
        print("None")
        return

    for post in data:
        print(post["data"]["title"])
