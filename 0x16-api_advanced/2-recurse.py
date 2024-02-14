#!/usr/bin/python3

""" A recursive function that queries the Reddit API and returns a list
    containing the titles of all hot articles for a given subreddit.
    If no results are found for the given subreddit,
    the function should return None
"""


import requests


def recurse(subreddit, hot_list=None, after=None):
    """
    Recursively queries the Reddit API and returns a list containing
    the titles
    of all hot articles for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit to query.
        hot_list (list): A list containing the titles of hot articles.
                         (default is None)
        after (str): A parameter for pagination. (default is None)

    Returns:
        list or None: A list containing the titles of hot articles if found,
                      otherwise None.
    """
    if hot_list is None:
        hot_list = []

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) \
               AppleWebKit/537.36"}
    params = {"limit": 100, "after": after}  # Fetch 100 posts per request

    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)

    if response.status_code == 404:
        return None

    data = response.json().get("data", {})
    posts = data.get("children", [])
    after = data.get("after")

    for post in posts:
        hot_list.append(post["data"]["title"])

    if after is not None:
        return recurse(subreddit, hot_list, after)
    else:
        return hot_list
