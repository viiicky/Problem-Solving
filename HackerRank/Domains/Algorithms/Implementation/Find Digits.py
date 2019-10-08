#!/bin/python3

import sys


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    
    '''
    number = int(n)
    counter = 0
    
    for d in n:
        digit = int(d)
        if digit == 0:
            pass
        elif not number % digit:
            counter += 1
            
    print(counter)
    '''
    
    print(len ([None for d in str(n) if d != '0' and n % int(d) == 0]))

