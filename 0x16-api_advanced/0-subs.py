import requests
import argv
'''
    Module contains that defines a function
    'number_of_subscribers'
'''


def number_of_subscribers(subreddit):

    '''
       This function returns the total number of subscribers
       for a subreddit
    '''
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {'User-Agent': 'Mozilla/5.0'}

    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        subscribers = data['data']['subscribers']
        return subscribers
    else:
        return 0


if __name__ == "__main__":
    number_of_subscribers(argv[1])
