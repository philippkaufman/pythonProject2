from math import sqrt, ceil

def deliteli(n):
    counter = 0
    a = 0
    b = 0
    for i in range(1, ceil(sqrt(n))):
        if n % i == 0:
            if i!= n//i:
                counter += 2
                if counter >= a:
                    a=counter
    print(n, a)


if __name__ =='__main__':
    for i in range(120115, 120200):
        deliteli(i)