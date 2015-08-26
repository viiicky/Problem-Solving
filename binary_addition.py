#!/usr/bin/env python3
# Adds two n bit binary numbers A and B and stores result in n+1 bit C
# Running time: O(n)
# by Vikas Prasad

# A = '1111'
# B = '1111'
while True:
    print('\nEnter equal length binary numbers:')
    A = input('A: ')
    B = input('B: ')
    i = len(A)
    C = [0] * (i + 1)

    carry = '0'
    for key in list(zip(A,B))[::-1]:
        temp = bin(int(key[0], 2) + int(key[1], 2) + int(carry, 2))
        if temp == '0b10' or temp == '0b11':
            carry = '1'
        else:
            carry = '0'
        C[i] = temp[-1]
        i -= 1
    if carry == '1':
        C[i] = 1

    for x in C:
        print(x, end='')
