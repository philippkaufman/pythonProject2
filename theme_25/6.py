from math import sqrt, ceil


def deliteli(n):
    numdel = 0
    a = 0
    denomimators = []
    for i in range(1, ceil(sqrt(n))):
        if n % i == 0:
            if i % 2 == 0:
                numdel += 1
                denomimators.append(i)
            if (n // i) % 2 == 0:
                numdel += 1
                denomimators.append(n // i)
    if numdel == 4:
        print(sorted(denomimators))


if __name__ == '__main__':
    for i in range(110203, 110245 + 1):
        deliteli(i)


