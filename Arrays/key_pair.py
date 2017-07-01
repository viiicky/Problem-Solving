# Given an array A[] and a number x, check for pair in A[] with sum as x
# Write a program that, given an array A[] of n numbers and another number x, determines whether or not there exist two elements in S whose sum is exactly x.
# Problem Link: http://www.geeksforgeeks.org/write-a-c-program-that-given-a-set-a-of-n-numbers-and-another-number-x-determines-whether-or-not-there-exist-two-elements-in-s-whose-sum-is-exactly-x/

T = int(input())

for _ in range(T):
    X = int(input().split()[1])
    A = [int(n) for n in input().split()]
    
    # create a hash table
    hash_table = {}
    
    # iterate the list
    for number in A:
        # insert the numberin hash_table
        hash_table[number] = True
        
        # check if the numbers complement is present in the list
        if X-number in hash_table:
            print("Yes")
            break
    else:
        print("No")