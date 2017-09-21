#!/usr/bin/python3
import requests


def top_ten(subreddit):
    """ queries Reddit API and prints the titles of
    first 10 hot posts listed for a given subreddit.

    If not a valid subreddit, print None.
    Ensure that you are not following redirects.
    """
    url = "http://www.reddit.com/r/{:s}/about.json".format(subreddit)
    headers = {'user-agent': 'egsyquest'}
    r = requests.get(url, headers=headers)

    if (r.status_code is 302):
        return 0
    if (r.status_code is 404):
        return 0

    r.json()
