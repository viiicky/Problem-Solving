#!/usr/bin/env python3
# Quick sort is another comparison sort, and is often best practical choice for sorting,
# because it is very efficient on average. Also, it sorts in place.
#
# Like merge sort, it also wroks on divide and conquer concept.
# The partition procedure is used to get a pivot and then the sub problems,
# generated around both sides of the pivot are solved.
# 
# If n is the number of elements in the list, worst case arises when the pivot is worst balanced,
# i.e. when pivot results in 0:n-1 size sublists(or, 0:n size sublists in case of hoarse implementation(see below for details)).
# If this worst case arises at each level of recursion, which is a very unlikely case,
# then the running time would fall to quadratic time.
#
# This situation tend to arise when the elements near each other are relatively not much unsorted.
# Thus one worst case scenario occurs when all the elements values are equal.
# Another such case is when the list is already sorted in either order.
#
# The latter case can be solved by introducing randomness to the list(assuming most of the list elements are distinct),
# like by shuffling the input list or by using random sampling.
# The former case, however is much complicated.
# Randomized version is better suited for large enough inputs.
#
# Also, for almost already sorted list, insertion sort tends to decrease towards O(n),
# that beats quick sort.
#
# Quick Sort Worst Running Time: O(n^2)
# Best Running Time: O(n lgn)
# Unlike other sorting techniques, the average case of quick sort is
# more close to best case, instead of worst case, because of the highly unlikely condition for worst case.
# Thus, Average Running Time: O(n lgn)
# by Vikas Prasad
# 27 Aug 2015

from random import randint      # this seeds also, according to docs

def quick_sort(A, p, r):
    if p < r:
        q = partition(A, p, r)
        quick_sort(A, p, q-1)
        quick_sort(A, q+1, r)

def partition(A, p, r):
    x = A[r]
    i = p - 1
    for j in range(p, r):
        if A[j] <= x:
            i += 1
            A[i], A[j] = A[j], A[i]

    A[i+1], A[r] = A[r], A[i+1]
    return i + 1

def randomized_partition(A, p, r):
    # random sampling
    i = randint(p, r)    #randint() includes end-points
    A[i], A[r] = A[r], A[i]
    return partition(A, p, r)

def randomized_quick_sort(A, p, r):
    if p < r:
        q = randomized_partition(A, p, r)
        randomized_quick_sort(A, p, q-1)
        randomized_quick_sort(A, q+1, r)

def hoare_partition(A, p, r):
    x = A[p]
    i = p - 1
    j = r + 1
    while True:
        j -= 1
        while A[j] > x:
            j -= 1
        i += 1
        while A[i] < x:
            i += 1
        if i < j:
            A[i], A[j] = A[j], A[i]
        else:
            return j

def hoare_quick_sort(A, p, r):
    if p < r:
        q = hoare_partition(A, p, r)
        hoare_quick_sort(A, p, q)
        hoare_quick_sort(A, q+1, r)

if __name__ == '__main__':
    # A = [2, 8, 7, 1, 3, 5, 6, 4]
    A = [13, 19, 9, 5, 12, 8, 7, 4, 21, 2, 6, 11]
    print(A)
    randomized_quick_sort(A, 0, len(A)-1)
    print(A)
