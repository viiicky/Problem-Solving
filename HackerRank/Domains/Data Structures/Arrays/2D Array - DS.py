#!/bin/python3

import sys


arr = []
for arr_i in range(6):
   arr_t = [int(arr_temp) for arr_temp in input().strip().split(' ')]
   arr.append(arr_t)

size = 6
max_hourglass_sum = -float('Infinity')
for i in range(size-2):
    # for vertical traversal
    # for size 6, i = 0, 1, 2, 3
    
    for j in range(1, size-1):
        # for horizontal traversal
        # for size 6, j = 1, 2, 3, 4
        sum = arr[i][j-1] + arr[i][j] + arr[i][j+1] + arr[i+1][j] + arr[i+2][j-1] + arr[i+2][j] + arr[i+2][j+1]
        if sum > max_hourglass_sum:
            max_hourglass_sum = sum

print(max_hourglass_sum)
