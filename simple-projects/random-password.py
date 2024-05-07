import secrets
import string
import sys


def go():
    required_password_length = input('Password length? [Default 8 characters] ')
    if len(required_password_length) == 0:
        password_length = 8
    elif not required_password_length.isdigit():
        print('Enter digit for password length.')
        sys.exit()
    else:
        password_length = int(required_password_length)

    include_digits = input('Include digits? [Default y] ').lower() or 'y'
    include_lower_case_letters = input('Include lower case letters? [Default y] ').lower() or 'y'
    include_upper_case_letters = input('Include upper case letters? [y/n] ').lower()
    include_symbols = input('Include symbols? [y/n] ').lower()

    # validate
    include_digits = 'y' if include_digits == 'y' else 'n'
    include_lower_case_letters = 'y' if include_lower_case_letters == 'y' else 'n'
    include_upper_case_letters = 'y' if include_upper_case_letters == 'y' else 'n'
    include_symbols = 'y' if include_symbols == 'y' else 'n'

    print('You have selected:')
    print(f'Password length? {password_length}')
    print(f'Include digits? {include_digits}')
    print(f'Include lower case letters? {include_lower_case_letters}')
    print(f'Include upper case letters? {include_upper_case_letters}')
    print(f'Include symbols? {include_symbols}')

    character_set = ''
    password = ''

    if include_digits == 'y':
        character_set += string.digits
        password += string.digits[secrets.randbelow(len(string.digits))]
    if include_lower_case_letters == 'y':
        character_set += string.ascii_lowercase
        password += string.ascii_lowercase[secrets.randbelow(len(string.ascii_lowercase))]
    if include_upper_case_letters == 'y':
        character_set += string.ascii_uppercase
        password += string.ascii_uppercase[secrets.randbelow(len(string.ascii_uppercase))]
    if include_symbols == 'y':
        character_set += string.punctuation
        password += string.punctuation[secrets.randbelow(len(string.punctuation))]

    character_set_length = len(character_set)
    for i in range(password_length - len(password)):
        password += character_set[secrets.randbelow(character_set_length)]

    print(f'Password: {password}')


if __name__ == '__main__':
    go()
