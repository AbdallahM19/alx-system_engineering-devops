#!/usr/bin/python3
"""
Write a function that queries the Reddit API,
returns the number of subscribers
"""

import requests


def number_of_subscribers(subreddit):
    """returns the number of subscribers else 0"""
    if subreddit is None or type(subreddit) is not str:
        return 0
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "Brave/1.65.126"}
    x = requests.get(url, headers=headers, allow_redirects=False)
    if x.status_code != 200:
        return 0
    else:
        i = x.json()
        return i['data']['subscribers']
