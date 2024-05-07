#!/usr/bin/python3
"""
Write a function that queries the Reddit API
prints the titles of the first 10 hot posts
listed for a given subreddit.
"""


import requests


def top_ten(subreddit):
    """prints the titles of the first 10 hot posts else 0"""
    if subreddit is None or not isinstance(subreddit, str):
        print('None')
    url = "https://www.reddit.com/r/{}/hot/.json?limit=10".format(
        subreddit
    )
    header_Agent = {"User-Agent": "Brave version 1.65.126"}
    response = requests.get(
        url,
        headers=header_Agent
    )
    data = response.json()
    posts = data["data"]["children"]
    i = 0
    titles_list = []
    for n in posts:
        if i < 10:
            titles_list.append("{}".format(str(n["data"]["title"])))
            i += 1
    for title in titles_list:
        print(title)
