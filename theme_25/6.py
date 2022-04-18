from math import sqrt, ceil
def deliteli(n):
    numdel = 0
    a = 0
    for i in range(2, ceil(sqrt(n))):
        if n%i ==0 and i%2 == 0:
            numdel +=1
            a = n
    if numdel == 4:
        print(a)



if __name__ =='__main__':
    for i in range(110203, 110245):
        deliteli(i)