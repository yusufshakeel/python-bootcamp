import requests


def go():
    payload = { 'foo': 'bar' }
    r = requests.post(
        'https://httpbin.org/post',
        json=payload
    )
    if r.status_code == requests.codes.ok:
        print(r.json())
    else:
        print('something went wrong')


if __name__ == '__main__':
    go()
