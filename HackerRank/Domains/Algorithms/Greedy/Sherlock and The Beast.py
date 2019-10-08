#!/bin/python3

import sys


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    
    number = ''
    for _ in range(n):
        number += '5'
        
    count_of_5 = n
    count_of_3 = 0

    while True:
        if not count_of_5 % 3:
            if not count_of_3 % 5:
                print(number)
                break
        else:
            if count_of_5 < 5:
                print(-1)
                break
            else:
                count_of_3 += 5
                count_of_5 -= 5
                number = '5'*count_of_5 + '3'*count_of_3
                

