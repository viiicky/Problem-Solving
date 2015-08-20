#!/usr/bin/env python3
# Linear search which searches for the position of a value(v) in a given sequence A
# having n number of elements.
# Prints None if v is not present in A at all.
# Worst & Average running time: O(n)
# Best running time: O(1)

while True:
    try:
        A = [int(x) for x in input('Enter numbers separated by space(q to exit): ').split()]
    except ValueError:
        exit('Exiting...')
    v = int(input('Enter the value to search for: '))
    # A = [5, 2, 4, 6, 1, 3]
    # v = 3

    for i, key in enumerate(A):
        if v == key:
            print(i)
            break
    else:
        print(None)
