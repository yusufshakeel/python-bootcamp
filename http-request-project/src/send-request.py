import pprint

import requests

BASE_URL: str = 'https://httpbin.org'


def handle_response(r):
    if r.status_code == requests.codes.ok:
        pprint.pprint(r.json())
    else:
        print('something went wrong')


def post():
    payload = {'foo': 'bar'}
    r = requests.post(
        f'{BASE_URL}/post',
        json=payload
    )
    handle_response(r)


def get():
    query_string = {'foo': 'bar'}
    r = requests.get(
        f'{BASE_URL}/get',
        params=query_string
    )
    handle_response(r)


if __name__ == '__main__':
    post()
    get()
