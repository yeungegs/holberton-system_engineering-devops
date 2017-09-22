#!/usr/bin/python3
import requests


def recurse(subreddit, hot_list=[]):
    """queries Reddit API and returns list containing the titles of
    all hot articles for a given subreddit

    Ensure that you are not following redirects.

    Returns:
        If no results are found for given subreddit, return None
        If not a valid subreddit, return None.
    """
    
