def f():
    with open('C:/Users/Виктория/Desktop/24_33.txt') as f:
        txt = f.readline()
        a = 0
        counta = 0
        max = 0
        for i in range(len(txt)):
            if txt[i] != 'E':
                a+=1
            if a>max:
                max = a
            if txt[i] == 'E':
                break
            if txt[i] == 'A':
                counta +=1
            if counta < 3
    print(max)







if __name__ == '__main__':
    f()