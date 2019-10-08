#!/bin/python3

import sys


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    
    '''
    height = 1
    for cycle in range(1, n+1):
        if cycle % 2:
            height *= 2
        else:
            height += 1
            
    print(height)
    '''
    
    '''Inspired by asbear'''
    print((2**(n//2 + 1) - 1) * (n%2 + 1))

