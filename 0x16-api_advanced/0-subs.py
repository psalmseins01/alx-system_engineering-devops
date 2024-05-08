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
    user = {'User-Agent': 'Lizzie'}
    endpoint = requests.get('https://www.reddit.com/r/{}/about.json'
                            .format(subreddit), headers=user).json()
    try:
        return endpoint.get('data').get('subscribers')
    except Exception:
        return 0


if __name__ == "__main__":
    number_of_subscribers(argv[1])
