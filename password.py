import random
from charsets import CHARSET


class Password:
    def __init__(self, _length_, _count_):
        self._length_ = _length_
        self._count_ = _count_

    def password_gen(self):
        for i in range(1, self._count_):
            password = str()
            for n in range(1, self._length_):
                char = random.choice(CHARSET)
                password = password + char
            print(password)


if __name__ == '__main__':
    Password(_length_=None, _count_=None)
