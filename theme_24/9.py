def f():
    with open('../sources/theme 24/24_9.txt', 'r') as f:
        txt = f.readline()
        maxlen = 1
        a = 0
        for i in txt:
            if i == 'C':
                a += 1
                maxlen = max(a, maxlen)
            else:
                a = 0

        print(maxlen)


if __name__ == '__main__':
    f()
