#!/usr/bin/python3
import requests


def recurse(subreddit, hot_list=[], after=""):
    """queries Reddit API and returns list containing the titles of
    all hot articles for a given subreddit

    Ensure that you are not following redirects.

    Returns:
        If no results are found for given subreddit, return None
        If not a valid subreddit, return None.
    """
    url_base = 'http://www.reddit.com/r/'
    url_query = '{:s}/hot.json'.format(subreddit)
    headers = {'user-agent': 'starcraft'}
    r = requests.get(url_base + url_query, headers=headers)

    if (r.status_code is 302):
        print("None")
        return
    if (r.status_code is 404):
        return None
    else:
        r = r.json()
        for post in r['data']['children']:
            hot_list.append(post['data']['title'])

    return recurse(subreddit, hot_list, after)
