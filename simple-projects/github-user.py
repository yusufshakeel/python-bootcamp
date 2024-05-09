from pprint import pprint

import requests


def go():
    username = input('Enter username: ')
    if len(username) == 0:
        raise Exception('username missing.')

    response = requests.get(f'https://api.github.com/users/{username}')

    if response.status_code != requests.codes.ok:
        print(f'User by username {username} not found')

    pprint(response.json())

if __name__ == '__main__':
    go()