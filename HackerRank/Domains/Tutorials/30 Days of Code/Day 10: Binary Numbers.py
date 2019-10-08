#!/bin/python3

import sys


n = int(input().strip())
binary = format(n, 'b')

count = 0
max_count = float('-Infinity')
for bit in str(binary.rstrip('0')):
    if (bit == '1'):
        count += 1
        
        if count > max_count:
            max_count = count
            
    elif (bit == '0'):
        count = 0
        
print(max_count)
