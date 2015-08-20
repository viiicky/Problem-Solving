#!/usr/bin/env python3
# Merge sort uses a recursive technqiue, divide & conquer
# It means dividing the given problem, into subproblem of same instance recursively
# Until, we reach a base case where number of elements in the sub problem is only 1
# And because of the fact, that 1 element squence is already sorted we simply return.
# Once two subproblems are solved we combine their solutions to find the solution of the parent problem.
# Running Time: O(n lgn), where n is the number of elements to be sorted.

def merge(A, p, q, r):
    # Filling the subarrays L and R with elements of A
    # n1 = q - p + 1
    # n2 = r - q
    L = []
    R = []
    for key in A[p : q+1]:
        L.append(key)
    for key in A[q+1 : r+1]:
        R.append(key)
    L.append(float('Infinity')) # appending sentinels at the end
    R.append(float('Infinity'))
 
    # Merging sorted elements from L and R back to A
    i = j = 0
    for k in range(p, r+1):
        # Test if no sentinels are used
        #if i >= n1:
        #    while j < n2:
        #        A[k] = R[j]
        #        k += 1
        #        j += 1
        #    return
        #if j >= n2:
        #    while i < n1:
        #        A[k] = L[i]
        #        k += 1
        #        i += 1
        #    return

        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1

def merge_sort(A, p, r):
    if p < r:   # if more than one elements
        q = (p + r) // 2
        merge_sort(A, p, q)
        merge_sort(A, q+1, r)
        merge(A, p, q, r)
    # print(A)

while True:
    A = [int(x) for x in input('Enter integers separated by space: ').split()]
    # A = [5, 2, 4, 7, 1, 3, 2, 6]
    merge_sort(A, 0, len(A)-1)
    print(A)
