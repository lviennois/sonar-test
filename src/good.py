def some_good_code(a=None):
    if a is None:
        a = ['hello']
    a.append('world')
    print(a)


if __name__ == '__main__':
    some_good_code()
