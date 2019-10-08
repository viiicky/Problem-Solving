#!/bin/python3

import sys

def sum_to_N(N):
    return N * (N+1) // 2

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    
    n -= 1
    print(3*(sum_to_N(n//3)) + 5*(sum_to_N(n//5)) - 15*(sum_to_N(n//15)))
