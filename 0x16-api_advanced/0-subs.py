#!/usr/bin/python3
"""Queries Reddit API"""

import requests


def number_of_subscribers(subreddit):
    """Return number of subscribers for a given subreddit"""

    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0"
    }

    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        try:
            result = response.json().get("data")
            return result.get("subscribers")
        # handle unexpected JSON structure
        except (AttributeError, KeyError):
            return 0
    else:
        return 0
