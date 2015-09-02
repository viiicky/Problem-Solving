#!/usr/bin/env python3
# Insertion sort uses an incremental approach. It is a comparison sort.
# Usually efficient for sorting a small numbers of elements.
# Or for nearly already sorted list
# If n is the number of elements, then:
# Worst Running Time: O(n^2), a quadratic function
# Best Running Time: O(n), a linear function
# by Vikas Prasad

def iterative_insertion_sort(A):
    '''Sort A iteratively.'''
    for i, key in enumerate(A[1:]):
        while i > -1 and A[i] > key:
            A[i + 1] = A[i]
            i = i - 1
        A[i + 1] = key

def insert(n):
    '''Insert the value at nth position in A, in the correct position in the sorted subarray A[: n]'''
    key = A[n]
    for i in reversed(range(n)):
        while i > -1 and A[i] > key:
            A[i + 1] = A[i]
            i -= 1
        A[i + 1] = key
        return

def recursive_insertion_sort(A):
    '''Sort A recursively, with the help of insert()'''
    if len(A) > 1:
        recursive_insertion_sort(A[: - 1])
        n = len(A[: -1])
        insert(n)

if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(description='sorts A using insertion sort, iterative in nature by default')
    group = parser.add_mutually_exclusive_group()
    group.add_argument('-r', '--recursive', action='store_true', help='uses a recursive approach for sorting')
    group.add_argument('-i', '--iterative', action='store_true', help='uses a iterative approach for sorting')
    parser.add_argument('elements', metavar='A', type=float, nargs='+', help='sequence of elements to be sorted')

    args = parser.parse_args()
    A = args.elements
    # A = [5, 2, 4, 6, 1, 3]
    if args.recursive:
        print('Sorting recursively...')
        recursive_insertion_sort(A)
    else:
        print('Sorting iteratively...')
        iterative_insertion_sort(A)
    print(A)
