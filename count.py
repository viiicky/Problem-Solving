#!/usr/bin/env python3
# This script tells the number of elements, that fall in the range [a..b] for n given integers. Integers are in the range 0 to k.
# Running Time: theta(k + n)
# Vikas Prasad
# 29 Aug 2015

def count(A, k, a, b):
    '''Return number of elements present in A in the range [a..b]'''
    # auxiliary array to hold the information,
    # that how many values in A are smaller than or equal to each element in the list A.
    C = [0] * (k + 1)

    for x in A:
        C[x] = C[x] + 1
    # now C holds the infomration how many times each element is present in A.

    for i in range(1, k + 1):
        C[i] = C[i] + C[i - 1]
    # now C holds the infomation how many elements are smaller or equal to each element in A.

    if a - 1 < 0:
        numberOfElements = C[b]
    else:
        numberOfElements = C[b] - C[a - 1]

    return numberOfElements

if __name__ == '__main__':
    # A = [2, 5, 3, 0, 2, 3, 0, 3]
    # print(A)
    # print(count(A, 5, 0, 5))

    A = [6, 0, 2, 0, 1, 3, 4, 6, 1, 3, 2]
    print(A)
    print(count(A, 6, 0, 6))
