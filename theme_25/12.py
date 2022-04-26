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
    if a == 2:
        print(n)


if __name__ =='__main__':
    for i in range(2422000, 2422080):
        deliteli(i)

