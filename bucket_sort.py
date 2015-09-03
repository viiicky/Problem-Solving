#!/usr/bin/env python3
# Bucket sort assumes that the input elements are distributed uniformly and independently over the interval [0,1)
# If n is the number of input elements, then
# it divides the interval into n equal sized buckets.
# As the inputs are assumed to be distributed uniformly and independently, we do not expect much crowd in a bucket.
# Worst case occurs when all the elements fall in a single bucket.
# Like radix sort, it also uses an intermediate sort to sort each bucket..
# Considering the intermediate sort to be insertion sort.
# Worst Running Time: theta(n^2)
# Average Running Time: theta(n)
# Vikas Prasad

try:
    from insertion_sort import iterative_insertion_sort
    from link_list import *
except ImportError:
    print('You need to make sure you have following modules, to run this script.')
    print('insertion_sort: https://github.com/viiicky/Algorithms-Python/blob/master/insertion_sort.py')
    print('link_list: https://github.com/viiicky/Algorithms-Python/blob/master/link_list.py')
    print('Please download the same and try again.')
    exit()

def bucket_sort(A): 
    n = len(A)
    B = [lList() for _ in range(n)]
    for x in A:
        l = link(x)
        B[int(n*x)].list_insert(l)

    for x in B:
        iterative_insertion_sort(x)

    sortedA = [float(str(y)) for x in B for y in x]
    print(sortedA)

if __name__ == '__main__':
    A = [.78, .17, .39, .26, .72, .94, .21, .12, .23, .68]
    # A = [.79, .13, .16, .64, .39, .20, .89, .53, .71, .42]
    print(A)
    bucket_sort(A)
