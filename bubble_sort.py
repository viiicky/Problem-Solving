#!/usr/bin/env python3
# Bubble sort is a simple, popular but inefficient sorting technique.
# Works by repeatedly swapping adjacent elemets that are out of order.
# Worst Case Running Time: O(n^2)
# Compared to worst case of insertion sort, it is yet inefficient because
# of the fact that swapping takes much more time than just moving elements.
# Even in the best case comparison, it is much inefficient than insertion sort,
# because it takes way more comparisons than insertion sort.
# by Vikas Prasad

import argparse

parser = argparse.ArgumentParser(description='Sorts A using bubble sort')
parser.add_argument('integers', metavar='A', type=int, nargs='+', help='list of integers to be sorted')
args = parser.parse_args()

A = args.integers
# A = [5, 2, 4, 3, 1, 6]
length = len(A)
for i in range(length-1):
    for j in reversed(range(i+1, length)):
        if A[j] < A[j - 1]:
            A[j], A[j-1] = A[j-1], A[j]
print(A)
