#!/usr/bin/env python3
# Radix sort uses an intermediate sort to sort the elements wrt to their digits.
# It starts sorting the elements with their least significant digit and then
# moving each bits towards the most significant one for the successice sorts.
# As a result when elements are sorted with respect to most significant digit the elements are completely sorted in all.
# It is important that the intermediate sort used is stable in nature.
# If d is the number of digits in the elements,
# and each digit can take k possible values,
# then Running Time: theta(d(n + k)),
# if the stable sort takes theta(n + k) time.
# Vikas Prasad
# 30 Aug 2015

def stable_sort(A, k, i):
    '''It is a variant of counting sort to aid radix sort.'''
    # auxiliary array to hold the information about digit at ith place in elements of A
    C = [0] * (k + 1)

    col = [int((str(x)[i])) for x in A] # this extracts the digit from ith place in elements of A
    data = zip(A, col)   # this holds elements of A with digit at their ith position

    for x in col:
        C[x] = C[x] + 1
    # now C holds the infomration how many times each digit at ith place in elements is present.

    for j in range(1, k + 1):
        C[j] = C[j] + C[j - 1]
    # now C holds the infomation how many digits are smaller or equal to other digits at the ith place in elements in A.

    for value, digit in reversed(list(data)):       # traversing in backward direction maintains stability.
        A[C[digit] - 1] = value 
        C[digit] -= 1

def radix_sort(A, d):
    k = 9
    for i in reversed(range(d)):
        stable_sort(A, k, i)
        # print(A)
    print(A)

if __name__ == '__main__':
    A = [329, 457, 657, 839, 436, 720, 355]
    d = 3
    print(A)
    radix_sort(A, d)
