def f():
    with open('C:/Users/Виктория/Desktop/24_18.txt', 'r') as f:
        txt = f.readline()
        rasst = 0
        for i in range(len(txt)):
            for r in range(1000):
                if not(25*'A') in f.readline(i):
                    if txt[i]==txt[r] and i != r:
                        rasst = r-i
                        print(rasst)















if __name__ == '__main__':
    f()