from time import monotonic


def rotate_left(triple):
    a, b, c = triple
    return b, c, a


def rotate_right():
    for i in range(1_000_000):
        pass

    return 'done'


if __name__ == '__main__':
    t1 = monotonic()
    print(rotate_right())
    t2 = monotonic()
    print(t2 - t1)
