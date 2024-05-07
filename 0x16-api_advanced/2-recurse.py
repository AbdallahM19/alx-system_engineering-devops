#!/usr/bin/python3
"""
Using reddit's API
"""


import requests


def recurse(subreddit, hot_list=[], after=None):
    """returning top ten post titles recursively"""
    if subreddit is None or not isinstance(subreddit, str):
        return None
    url = "https://www.reddit.com/r/{}/hot.json".format(
        subreddit
    )
    headers = {"User-Agent": "Brave version 1.65.126"}
    params = {"after": after}
    response = requests.get(url, headers=headers, params=params)
    if response.status_code != 200:
        return None
    data = response.json()
    posts = data["data"]["children"]
    after = data["data"]["after"]
    for post in posts:
        hot_list.append(post["data"]["title"])
    if after:
        recurse(subreddit, hot_list, after)
    return hot_list
