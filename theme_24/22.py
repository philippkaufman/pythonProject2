def count_g(line):
    counter = 0
    for letter in line:
        if letter == 'G':
            counter += 1
    return counter


def find_max_letter(line):
    bukv = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0, 'G': 0, 'H': 0, 'I': 0, 'J': 0, 'K': 0, 'L': 0, 'M': 0,
            'O': 0, 'P': 0, 'Q': 0, 'R': 0, 'S': 0, 'T': 0, 'U': 0, 'V': 0, 'W': 0, 'X': 0, 'Y': 0, 'Z': 0, }
    for i in line:
        bukv[i] += 1
    max_value = 0
    lettr = ''
    for key, value in bukv.items():
        if value > max_value:
            max_value = value
            lettr = key

    return lettr


def fun():
    with open('../sources/theme 24/24_22.txt', 'r') as f:
        min_count = 100000000000
        min_line = ''
        for line in f.readlines():
            counter = count_g(line)
            if counter < min_count:
                min_count = counter
                min_line = line

        letter = find_max_letter(min_line)

        print(letter)


if __name__ == '__main__':
    fun()
