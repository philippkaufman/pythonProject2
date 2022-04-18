def f():
    with open('C:/Users/Виктория/Desktop/24_20.txt', 'r') as f:
        txt = f.read()
        A=0
        B=0
        C=0
        D=0
        E=0
        F=0
        G=0
        H=0
        I=0
        J=0
        K=0
        L=0
        M=0
        N=0
        O=0
        P=0
        Q=0
        R=0
        S=0
        T=0
        U=0
        V=0
        W=0
        X=0
        Y=0
        Z=0
        for i in range(len(txt)-2):
            if txt[i] == txt[i+2] and txt[i+1] == 'A':
                A += 1
            if txt[i] == txt[i+2] and txt[i+1] == 'B':
                B += 1
            if txt[i] == txt[i+2] and txt[i+1] == 'C':
                C += 1
            if txt[i] == txt[i+2] and txt[i+1] == 'D':
                D += 1
            if txt[i] == txt[i+2] and txt[i+1] == 'E':
                E += 1
            if txt[i] == txt[i+2] and txt[i+1] == 'F':
                F += 1
            if txt[i] == txt[i+2] and txt[i+1] == 'G':
                G += 1
            if txt[i] == txt[i+2] and txt[i+1] == 'H':
                H += 1
            if txt[i] == txt[i+2] and txt[i+1] == 'I':
                I += 1
            if txt[i] == txt[i+2] and txt[i+1] == 'J':
                J += 1
            if txt[i] == txt[i+2] and txt[i+1] == 'K':
                K += 1
            if txt[i] == txt[i+2] and txt[i+1] == 'L':
                L += 1
            if txt[i] == txt[i+2] and txt[i+1] == 'M':
                M += 1
            if txt[i] == txt[i+2] and txt[i+1] == 'N':
                N += 1
            if txt[i] == txt[i+2] and txt[i+1] == 'O':
                O += 1
            if txt[i] == txt[i+2] and txt[i+1] == 'P':
                P += 1
            if txt[i] == txt[i+2] and txt[i+1] == 'Q':
                Q += 1
            if txt[i] == txt[i+2] and txt[i+1] == 'R':
                R += 1
            if txt[i] == txt[i+2] and txt[i+1] == 'S':
                S += 1
            if txt[i] == txt[i+2] and txt[i+1] == 'T':
                T += 1
            if txt[i] == txt[i+2] and txt[i+1] == 'U':
                U += 1
            if txt[i] == txt[i+2] and txt[i+1] == 'V':
                V += 1
            if txt[i] == txt[i+2] and txt[i+1] == 'W':
                W += 1
            if txt[i] == txt[i+2] and txt[i+1] == 'X':
                X += 1
            if txt[i] == txt[i+2] and txt[i+1] == 'Y':
                Y += 1
            if txt[i] == txt[i+2] and txt[i+1] == 'Z':
                Z += 1

    print(A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R, S, T, U, V, W, X, Y, Z)


if __name__ == '__main__':
    f()