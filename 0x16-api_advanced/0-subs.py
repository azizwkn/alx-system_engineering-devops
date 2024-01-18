#!/usr/bin/python3
"""Queries Reddit API"""

import requests


def number_of_subscribers(subreddit):
    """Return number of subscribers"""

    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {
                "Uer-Agent": "api_advanced"
    }

    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        try:
            result = response.json().get("data")
            return result.get("subscribers")

        except KeyError:
            return 0
    else:
        return 0
