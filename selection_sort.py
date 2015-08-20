#!/usr/bin/env python3
# Selection sort
# Worst Running Time: O(n^2)
# Best Running Time: O(n^2), because of the fact that even if the element at i is already the smallest,
# we have to go all the way long to check for the same.

while True:
    A = [int(x) for x in input('Enter integers separated by space: ').split()]
    # A = [5, 2, 4, 6, 1, 3]

    for i in range(len(A)-1):
        least = A[i]
        pos = i
        j = i + 1
        while j <= len(A)-1:    # Finding the smallest value in the subarray A[i+1 :]
            if least > A[j]:
                least = A[j]
                pos = j
            j += 1
        A[i], A[pos] = A[pos], A[i]     # Exchanging the smallest value found with the value at ith position
    
    print(A)
