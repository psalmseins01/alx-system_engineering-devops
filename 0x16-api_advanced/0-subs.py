#!/usr/bin/python3
'''
    Module contains that defines a function
    'number_of_subscribers'
'''
import requests
from sys import argv


def number_of_subscribers(subreddit):
    '''
       This function returns the total number of subscribers
       for a subreddit
    '''
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    headers = {
        "User-Agent": "Linux: 0x16.api.advanced"
        }
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code != requests.codes.ok:
        return 0
    results = response.json().get('data')
    return results.get('subscribers')


if __name__ == "__main__":
    number_of_subscribers(argv[1])
