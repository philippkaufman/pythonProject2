def f():
    with open('C:/Users/Виктория/Desktop/24_33.txt') as f:
        txt = f.readline()
        len = 0
        count_A = 0
        max_len = 0
        for i in txt:
            if i == 'E':
                if count_A < 3:
                    len = 0
                    count_A = 0
                else:
                    max_len = max(len, max_len)
                    len = 0
                    count_A = 0
            elif i == 'A':
                count_A += 1
                len += 1
            else:
                len += 1
    print(max_len)


if __name__ == '__main__':
    f()
