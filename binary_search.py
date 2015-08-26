#!/usr/bin/env python3
# Recursive binary search
# If n is the total number of items, then:
# Worst Running Time: O(lgn)
# Best Running Time: O(1)
# An analogous example for binary search is searching
# for the meaning of a word in the dictionary
# or probably a name in a telephone directory
# by Vikas Prasad

def binary_search(A, v, p, q):
    mid = (p + q) // 2

    if q < p:
        return None
    if A[mid] == v:
        return mid
    if A[mid] < v:
        return binary_search(A, v, mid+1, q)
    else:
        return binary_search(A, v, p, mid-1)

import argparse

parser = argparse.ArgumentParser(description='finds the position of v in A')
parser.add_argument('integers', metavar='A', type=int, nargs='+', help='sequence of integers')
parser.add_argument('value', metavar='v', type=int, help='value whose position is to be searched in A')

args = parser.parse_args()
A = args.integers
v = args.value
# A = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# v = int(input())
print('Searching', v)
print('Found at', binary_search(A, v, 0, len(A)-1))
