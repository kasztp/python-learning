#!/bin/python3

import sys

if __name__ == "__main__":
    t = int(input().strip())
    for a0 in range(t):
        n = int(input().strip())
        arr = list(map(int, input().strip().split(' ')))

        instruments = 0
        assets = 0
        spending = 0
        profit = 0
        
        top = max(arr)
        for day in range(n):
            if arr[day] < top:
                spending -= arr[day]
                instruments += 1
            elif arr[day] == top:
                assets += (arr[day] * instruments)
                instruments = 0
                if day < n-1:
                    temp = day + 1
                    top = max(arr[temp:n])
        profit = spending + assets
        print(profit)
