def find_A(line):
    count_a = 0
    for i in line:
        if i == 'A':
            count_a += 1
    return count_a


def find_distance(line):
    bukv = {'A': [100000000, 0], 'B': [100000000, 0], 'C': [100000000, 0], 'D': [100000000, 0],
            'E': [100000000, 0],
            'F': [100000000, 0],
            'G': [100000000, 0],
            'H': [100000000, 0], 'I': [100000000, 0],
            'J': [100000000, 0], 'K': [100000000, 0], 'L': [100000000, 0], 'M': [100000000, 0],
            'O': [100000000, 0], 'P': [100000000, 0], 'Q': [100000000, 0], 'R': [100000000, 0],
            'S': [100000000, 0],
            'T': [100000000, 0],
            'U': [100000000, 0],
            'V': [100000000, 0], 'W': [100000000, 0],
            'X': [100000000, 0], 'Y': [100000000, 0], 'Z': [100000000, 0],}
    for i in range(len(line)):
        letter = line[i]
        bukv[letter][0] = min(bukv[letter][0], i)
        bukv[letter][1] = max(bukv[letter][1], i)
    max_distance = 0
    for key, value in bukv.items():
        max_distance = max(max_distance, value[1] - value[0])

    return max_distance


def f():
    with open('C:/Users/Виктория/Desktop/24_18.txt', 'r') as f:
        max_distance = 0
        for line in f.readlines():
            if find_A(line) < 25:
                distance = find_distance(line)
                max_distance = max(distance, max_distance)

        print(max_distance)


if __name__ == '__main__':
    f()
