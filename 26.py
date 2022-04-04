from math import sqrt, ceil


def get_denominator(number):
    denominator = 17
    while denominator < ceil(sqrt(number)):
        if n % denominator == 0:
            if denominator % 10 == 7:
                return denominator
        denominator += 10
    return 0


if __name__ == '__main__':
    i = 50
    n = 600000
    while i > 0:
        n += 1
        lowest_denominator = get_denominator(n)
        if lowest_denominator:
            print(n, lowest_denominator)
            i -= 1
