def add(*args):
    print('add', args, '=', sum(args))


def multiply(x, y):
    print('multiply', x, y, '=', x * y)


def collect(**kwargs):
    print(kwargs)


def collect2(*args, **kwargs):
    print(args)
    print(kwargs)


def main():
    add(10, 20, 30)
    multiply(**{'x': 10, 'y': 20})
    multiply(*[10, 20])
    collect(name='tintin', type='fiction')
    collect2(1, 2, 3, name='batman', type='fiction')


if __name__ == '__main__':
    main()
