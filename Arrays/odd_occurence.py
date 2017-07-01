# Find the Number Occurring Odd Number of Times
# Given an array of positive integers.
# All numbers occur even number of times except one number which occurs odd number of times.
# Find the number in O(n) time & constant space.
# Problem Link: http://practice.geeksforgeeks.org/problems/find-the-odd-occurence/0

from functools import reduce

def find_odd_occurence(array):
    hash_table = {}

    '''
    # This will work in O(n) time but will also take O(k) auxillary space.
    # where k is the number of distinct items present in the array.
    for item in array:
        if item in hash_table:
            hash_table.pop(item)
        else:
            hash_table[item] = True
    '''

    # doing XOR:
    '''
    xor = 0
    for item in array:
        xor ^= item

    return xor
    '''

    # using reduce with XOR:
    return reduce(lambda x, y: x^y, array)

    # using generator expression:
    # ((hash_table.pop(item)) if (item in hash_table) else (hash_table.update({item:True})) (for item in array))
    # (hash_table.update({item:True}) for item in array)
    # [hash_table.update({item:True}) for item in array]    # Ask on SO LC working but GE not
    # print(hash_table)

    # return next(iter(hash_table))

if(__name__ == '__main__'):
    T = int(input())

    for _ in range(T):
        input()
        array = [int(n) for n in input().split()]
        print(find_odd_occurence(array))
