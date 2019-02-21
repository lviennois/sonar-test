def some_bad_code(a=['hello']):
    a.append('world')
    print(a)


class BadClass:
    def __init__(self):
        self.a = 1
        return self


if __name__ == '__main__':
    some_bad_code()
