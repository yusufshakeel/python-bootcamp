import random


def go():
    while True:
        user_input: str = input('How many dices do you want to roll? [Type EXIT to end the game] ')
        if user_input == 'EXIT':
            print('Game ends here. Bye.')
            break

        try:
            number_of_dices = int(user_input)
            if number_of_dices < 1 or number_of_dices > 10:
                raise Exception('Enter integer value between 1 to 10')
        except ValueError:
            print('Enter integer value between 1 to 10')
            continue
        except Exception as e:
            print(e)
            continue

        dice_value: list[int] = []
        for i in range(number_of_dices):
            dice_value.append(random.randint(1, 6))

        print('You got the following numbers')
        print(dice_value)


if __name__ == '__main__':
    go()
