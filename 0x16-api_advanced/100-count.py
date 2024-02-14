#!/usr/bin/python3

"""
A recursive function that queries the Reddit API,
parses the title of all hot articles, and prints a sorted count of given
keywords (case-insensitive, delimited by spaces.
Javascript should count as javascript, but java should not)
"""


import requests
from collections import defaultdict


def count_words(subreddit, word_list, after=None, word_count=defaultdict(int)):
    """
    Recursively queries the Reddit API, parses the title of all hot articles,
    and prints a sorted count of given keywords.

    Args:
        subreddit (str): The name of the subreddit.
        word_list (list): A list of keywords to count occurrences of.
        after (str): A parameter for pagination. (default is None)
        word_count (dict): A dictionary to store word counts.
                           (default is defaultdict(int))

    Returns:
        None
    """
    if not word_list:
        return

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) \
               AppleWebKit/537.36"}
    params = {"limit": 100, "after": after}  # Fetch 100 posts per request

    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)

    if response.status_code == 404:
        return

    data = response.json().get("data", {})
    posts = data.get("children", [])
    after = data.get("after")

    for post in posts:
        title = post["data"]["title"].lower()
        for word in word_list:
            if f' {word.lower()} ' in f' {title} ':
                word_count[word.lower()] += title.count(f' {word.lower()} ')

    if after is not None:
        count_words(subreddit, word_list, after, word_count)
    else:
        sorted_counts = sorted(word_count.items(), key=lambda x: (-x[1], x[0]))
        for word, count in sorted_counts:
            print(f"{word}: {count}")
