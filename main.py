from password import Password


def main():
    length = int(input('Length: '))
    count = int(input('Count: '))
    password = Password(_length_=length, _count_=count)
    password.password_gen()


if __name__ == '__main__':
    main()
