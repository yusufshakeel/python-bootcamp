import random


def go():
    fruits = [
        'apple',
        'mango',
        'banana',
        'orange',
        'pineapple',
        'guava',
        'strawberry',
        'watermelon',
        'jackfruit',
        'avocado'
    ]

    random_fruit = random.choice(fruits)
    user_guessed_letters = ''
    user_remaining_wrong_guess_count = 5

    print('Welcome to hangman. Guess the name of the fruit letter by letter.')

    while user_remaining_wrong_guess_count > 0:
        print('Word ', end='')
        correct_guessed_letter_count = 0
        for ch in random_fruit:
            if ch in user_guessed_letters:
                print(ch, end='')
                correct_guessed_letter_count += 1
            else:
                print('_', end='')
        print() # new line

        if correct_guessed_letter_count == len(random_fruit):
            print('You guessed the fruit correctly!')
            break

        user_input: str = input('Enter a letter [Type 0 to end the game] ')
        if user_input == '0':
            print('Game ends here. Bye.')
            break
        elif len(user_input) != 1:
            print('Enter single character.')
            continue

        if user_input in user_guessed_letters:
            print(f'You have already guessed the letter {user_input}')
            continue
        elif user_input in random_fruit:
            user_guessed_letters += user_input

        if user_input not in random_fruit:
            user_remaining_wrong_guess_count -= 1
            print(f'Wrong letter. [Remaining tries: {user_remaining_wrong_guess_count}]')

        if user_remaining_wrong_guess_count == 0:
            print('Game Over!')
            print(f'The fruit was: {random_fruit}')
            break


if __name__ == '__main__':
    go()
