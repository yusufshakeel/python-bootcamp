import requests


def download_profile_image(username: str):
    github_user = requests.get(f'https://api.github.com/users/{username}')
    if github_user.status_code == requests.codes.ok:
        avatar_url = github_user.json()['avatar_url']
    else:
        print('username not found')
        return

    avatar_response = requests.get(avatar_url)

    try:
        if avatar_response.status_code == requests.codes.ok:
            file_type = avatar_response.headers['Content-Type']

            if file_type == 'image/png':
                file_extension = 'png'
            elif file_type == 'image/jpg' or file_type == 'image/jpeg':
                file_extension = 'jpg'
            else:
                raise Exception('unknown content type')

            with open(f'download.{file_extension}', 'wb') as file:
                for chunk in avatar_response.iter_content(chunk_size=100):
                    file.write(chunk)

    except Exception as e:
        print(f'Error {e}')


if __name__ == '__main__':
    username = input('Enter username: ')
    download_profile_image(username)
    print('done!')
