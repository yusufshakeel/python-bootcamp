from functools import reduce


def add():
    numbers = [1, 2, 3]
    print('add', numbers)
    return reduce(lambda acc, curr: acc + curr, numbers)


def multiply_numbers():
    numbers = [1, 2, 3, 4, 5]
    print('multiply_numbers', numbers)
    return reduce(lambda acc, curr: acc * curr, numbers)


def odd_numbers():
    numbers = [1, 2, 3, 4, 5, 6, 7]
    print('odd_numbers', numbers)
    return list(filter(lambda n: n % 2 != 0, numbers))


def greater_than_100():
    numbers = [10, 20, 100]
    print('greater_than_100', numbers)
    return list(filter(lambda n: n > 100, numbers))


def double_numbers():
    numbers = [1, 2, 3]
    print('double_numbers', numbers)
    return list(map(lambda n: n * 2, numbers))


def main():
    print('add using reduce', add())
    print('multiply numbers using reduce', multiply_numbers())
    print('find odd numbers using filter', odd_numbers())
    print('find numbers greater than 100', greater_than_100())
    print('doubles using map', double_numbers())


if __name__ == '__main__':
    main()
