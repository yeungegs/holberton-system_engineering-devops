#!/usr/bin/python3
import requests


def top_ten(subreddit):
    """ queries Reddit API and prints the titles of
    first 10 hot posts listed for a given subreddit.

    If not a valid subreddit, print None.
    Ensure that you are not following redirects.
    """
    url_base = 'http://www.reddit.com/r/'
    url_query = '{:s}/hot.json?limit={:d}'.format(subreddit, 10)
    headers = {'user-agent': 'egsyquest'}
    r = requests.get(url_base + url_query, headers=headers)

    if (r.status_code is 302):
        print("None")
        return
    if (r.status_code is 404):
        print("None")
        return
    else:
        r = r.json()
        for post in r['data']['children']:
            print(post['data']['title'])
