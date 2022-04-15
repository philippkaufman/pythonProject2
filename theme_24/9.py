def f():
    with open('C:/Users/Виктория/PycharmProjects/pythonProject/sources/theme 24/24_9.txt', 'r') as f:
        txt = f.readline()
        print(txt)
        maxlen = 1
        a = 1
        for i in range(2, len(txt)):
            if txt[i] == 'C' and txt[i+1] == 'C':
                a += 1
                maxlen = max(a, maxlen)
            else:
                a = 0

        print(maxlen)






    if __name__ == '__main__':
        f()