#!/usr/bin/env python3
# Given a package with a weight 'limit' and an array 'arr' of item
# weights, how can you most efficiently find two items with sum of
# weights that equals the weight limit?

# Question:

# Your function should return 2 such indices of item weights or -1 if
# such pair doesn't exist.
# What is the runtime and space complexity of your solution?

# Solution:

# The brute force solution is looping over the array and then for each
# weight looping on all other weights(ahead of it), while comparing
# the sum of each pair to the weight limit.
# It takes O(n2) runtime complexity.

# This is a classic case to use a hash table.
# We iterate over arr only once. For each weight w in arr we check if
# was hashed so far. If we find w in the hash table we return both
# indices, if not we hash the complement of w i.e. limit-w while using
# the complement as the hash key and the array index as the hash value
# (even if the same weight is found more than once it doesn't matter
# because at the time of the lookup we only need one product with that
# weight).
# Found this on pramp.com

# If n is the number of items and m is the number of distinct items,
# Time Complexity: O(n)
# Space Complexity: O(m)

def findComplementingWeights(arr, limit):
    hash_table= {}
    for index, item in enumerate(arr):
        if item in hash_table:
            return hash_table[item], index
        else:
            hash_table[limit - item] = index
    return -1

if __name__ == '__main__':
    arr = [2, 8, 7, 1, 3, 5, 6, 4]
    limit = 3
    print(findComplementingWeights(arr, limit))
