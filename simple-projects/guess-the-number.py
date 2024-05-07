from random import randint


def go():
    start, end = 1, 10
    random_number = randint(start, end)
    while True:
        try:
            guess = int(input(f'Guess the number between {start} and {end} both inclusive: '))
        except ValueError:
            print('Enter an integer number.')
            continue

        if guess == random_number:
            print('You have guessed the number!')
            print('Game ends here. Bye')
            break
        elif guess > random_number:
            print('Too high')
        else:
            print('Too low')


if __name__ == '__main__':
    go()