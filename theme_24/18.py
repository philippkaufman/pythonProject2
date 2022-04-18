def f():
    with open('C:/Users/Виктория/Desktop/24_18.txt', 'r') as f:
        result = {
            'A': 0,
            'B': 0,
            'C': 0,
            'D': 0,
            'E': 0,
            'F': 0,
            'G': 0,
            'H': 0,
            'I': 0,
            'J': 0,
            'K': 0,
            'L': 0,
            'M': 0,
            'N': 0,
            'O': 0,
            'P': 0,
            'Q': 0,
            'R': 0,
            'S': 0,
            'T': 0,
            'U': 0,
            'V': 0,
            'W': 0,
            'X': 0,
            'Y': 0,
            'Z': 0
        }
        txt = f.read()

        for i in range(len(txt)-1):
            if txt[i] == 'A':
                result[txt[i+1]] += 1

        max_value = 0
        letter = '1'
        for key, value in result.items():
            if value > max_value:
                max_value = value
                letter = key

    print(letter)

















if __name__ == '__main__':
    f()