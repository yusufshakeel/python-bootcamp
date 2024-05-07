def get_user_input() -> str:
    name = input("Enter your name: ")
    if len(name) == 0:
        raise Exception("Name missing.")
    return name


def go():
    name = get_user_input()
    print(f"Hello, {name}")


if __name__ == '__main__':
    go()
