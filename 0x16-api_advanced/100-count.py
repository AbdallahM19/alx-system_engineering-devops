#!/usr/bin/python3
"""
Write a recursive function that queries the Reddit API
"""


import requests


def count_words(subreddit, word_list, after=None, count_dict=None):
    """prints a sorted count of given keywords"""
    if count_dict is None:
        count_dict = {}
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
        title = post["data"]["title"].lower()
        for word in word_list:
            if word.lower() in title:
                count_dict[word] = count_dict.get(word, 0) + 1

    if after:
        count_words(subreddit, word_list, after, count_dict)

    if after is None:
        sorted_counts = sorted(
            count_dict.items(), key=lambda x: (-x[1], x[0])
        )
        for k, v in sorted_counts:
            print("{}: {}".format(k, v))
