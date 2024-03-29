#!/usr/bin/python3
"""contains the number of subscribers"""


import requests


def number_of_subscribers(subreddit):
    """returns the number of subscribers"""
    if not subreddit or type(subreddit) != str:
        return 0
    r = requests.get('http://www.reddit.com/r/{}/about.json'.format(subreddit),
                     headers={'User-Agent': '0x16-api_advanced:project:\
v1.0.0 (by /u/firdaus_cartoon_jr)'}).json()
    subs_count = r.get("data", {}).get("subscribers", 0)
    return subs_count
