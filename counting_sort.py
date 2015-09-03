#!/usr/bin/env python3
# Counting Sort
# Assuming each of the n input elements is an integer in the range 0 to k, where k = O(n),
# it sorts in linear time.
# Though the running time is theta(k+n), in practise, we usually use counting sort when k = O(n)
# thus Running Time: theta(n)
# This sorting technique is stable in nature.
# Counting sort assumes that input integers are in small range, i.e. k is not much big with respect to n.
# Please note that even if k exceeds O(n), the algorithm would work fine,
# but it should never go below 0, because the input elements itself are used for array subscripting.
# Vikas Prasad
# 29 Aug 2015

def counting_sort(A, B, k):
    # auxiliary array to hold the information,
    # that how many values in A are smaller than or equal to each element in the list A.
    C = [0] * (k + 1)

    for x in A:
        C[x] = C[x] + 1
    # now C holds the infomration how many times each element is present in A.

    for i in range(1, k + 1):
        C[i] = C[i] + C[i - 1]
    # now C holds the infomation how many elements are smaller or equal to each element in A.

    for x in reversed(A):       # traversing in backward direction helps in maintaining stability.
        B[C[x] - 1] = x
        C[x] -= 1

if __name__ == '__main__':
    # A = [6, 0, 2, 0, 1, 3, 4, 6, 1, 3, 2]
    A = [2, 5, 3, 0, 2, 3, 0, 3]
    B = [None] * len(A)
    print(A)
    counting_sort(A, B, 5)
    # counting_sort(A, B, 6)
    print(B)
