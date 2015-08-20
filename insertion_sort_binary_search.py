#!/usr/bin/env python3
# Sorts the given list using insertion sort and binary search
def binary_search(A, v, p, q):
    '''Search for the index to insert v in the sorted subarray A'''
    mid = (p + q) // 2

    if A[mid] == v:
        return mid + 1
    if A[mid] < v:
        if mid + 1 > q:
            return mid + 1
        elif A[mid+1] > v:
            return mid + 1
        else:
            return binary_search(A, v, mid+1, q)
    else:
        if mid - 1 < 0:
            return 0
        else:
            return binary_search(A, v, p, mid-1)

def insertion_sort(A):
    '''Sort A iteratively.'''
    for i, key in enumerate(A[1:]):
        pos = binary_search(A, key, 0, i)
        while i >= pos:
            A[i + 1] = A[i]
            i -= 1
        A[pos] = key
    # for i, key in enumerate(A[1:]):
        # while i > -1 and A[i] > key:
        #    A[i + 1] = A[i]
        #    i = i - 1
        # A[i + 1] = key

import argparse

parser = argparse.ArgumentParser(description='Sorts A using insertion sort but with binary search instead of linear')
parser.add_argument('integers', metavar='A', type=int, nargs='+', help='sequence of integers to be sorted')

args = parser.parse_args()
A = args.integers
# A = [5, 2, 4, 6, 1, 3]
insertion_sort(A)
print(A)
