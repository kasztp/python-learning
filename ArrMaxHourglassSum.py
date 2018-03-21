#!/bin/python3

import sys


arr = []
sums = []
for arr_i in range(6):
   arr_t = [int(arr_temp) for arr_temp in input().strip().split(' ')]
   arr.append(arr_t)

def hourglass(array,h,v):
    linesum_up = sum(array[v][h:h+3])
    linesum_bottom = sum(array[v+2][h:h+3])
    hourglass_sum = linesum_up + linesum_bottom + array[v+1][h+1]
    return(hourglass_sum)

for horizontal in range(4):
    for vertical in range(4):
        sums.append(hourglass(arr,horizontal,vertical))
result = max(sums)
print(result)
