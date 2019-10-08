#!/bin/python3

import sys


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    
    a = 1
    b = 2
    
    even_sum = b
    c = a + b
    
    while True:
        a = b
        b = c
        c = a + b
        
        if c > n:
            break
            
        if c % 2 == 0:
            even_sum += c
            
    print(even_sum)

