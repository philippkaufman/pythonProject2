from math import sqrt, ceil

def check(n):
    for i in reversed(range(ceil(sqrt(n))), 2):
        if n % i == 0:
            if i % 10 == 7:
                return i
    return 0


if __name__ == '__main__':
    i = 50
    n = 600000
    while i > 0:
        n += 1
        delitel = check(n)
        if delitel:
            print(n, delitel)
            i -= 1