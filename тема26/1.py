with open("C:/Users/Виктория/PycharmProjects/pythonProject/sources/theme_26/1.txt") as f:
    size = int(f.readline().split(' ')[0])
    a = [int(x) for x in f.readlines()]

a = sorted(a)
inform = 0
maxi = 0
for i in range(0, len(a)):
    if inform + a[i] <= size:
        inform += a[i]
        maxi += 1
print(maxi)


novi = a[maxi]
for i in range(maxi, len(a)):
    if inform - novi + a[i] <= size:
        inform = inform - novi + a[i]
        novi = a[i]

print(novi)

