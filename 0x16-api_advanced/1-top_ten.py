#!/usr/bin/python3
"""
Write a function that queries the Reddit API
prints the titles of the first 10 hot posts
listed for a given subreddit.
"""


from requests import get


def top_ten(subreddit):
    """prints the titles of the first 10 hot posts else 0"""
    if subreddit is None or type(subreddit) is not str:
        print('None')
    try:
        url = "https://www.reddit.com/r/{}/hot/.json?limit=10".format(
            subreddit
        )
        header_Agent = {"User-Agent": "Brave version 1.65.126"}
        x = get(url, headers=header_Agent)
        i = x.json()
        i = i['data']['children']
        for n in i:
            print(n['data']['title'])
    except Exception:
        print('None')
