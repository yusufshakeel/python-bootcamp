import requests


def go():
    query_string = { 'foo': 'bar' }
    headers = { 'x-my-token': '1234567890abcdef' }
    r = requests.get(
        'https://example.com',
        params=query_string,
        headers=headers
    )

    if r.status_code == requests.codes.ok:
        print(r.text)
    else:
        print('something went wrong')


if __name__ == '__main__':
    go()
