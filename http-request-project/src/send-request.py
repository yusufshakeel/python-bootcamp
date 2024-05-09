import pprint

import requests

BASE_URL = 'https://httpbin.org'
HEADERS = {
    'x-my-token': '0123456789abcdef'
}


def handle_response(r):
    if r.status_code == requests.codes.ok:
        pprint.pprint(r.json())
    else:
        print('something went wrong')


def post():
    payload = {'foo': 'bar'}
    r = requests.post(
        f'{BASE_URL}/post',
        json=payload,
        headers=HEADERS
    )
    handle_response(r)


def get():
    query_string = {'foo': 'bar'}
    r = requests.get(
        f'{BASE_URL}/get',
        params=query_string,
        headers=HEADERS
    )
    handle_response(r)


def post_form_data():
    form_data = {'foo': 'bar'}
    r = requests.post(
        f'{BASE_URL}/post',
        data=form_data,
        headers=HEADERS
    )
    handle_response(r)


if __name__ == '__main__':
    post()
    get()
    post_form_data()
