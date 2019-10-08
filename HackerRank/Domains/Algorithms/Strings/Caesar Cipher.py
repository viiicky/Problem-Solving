input()
S = input()
K = int(input()) % 26

S = list(S)
for i, item in enumerate(S):
    ascii = ord(item)
    if ascii in range(65, 91):
        ascii += K
        if ascii > 90:
            ascii -= 26
        S[i] = chr(ascii)
    elif ascii in range(97, 123):
        ascii += K
        if ascii > 122:
            ascii -= 26
        S[i] = chr(ascii)
            
for item in S:
    print(item, end='')
