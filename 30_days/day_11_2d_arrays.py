#!/bin/python3

import sys
# import numpy as np

arr = []
for arr_i in range(6):
    arr_t = [int(arr_temp) for arr_temp in input().strip().split(' ')]
    arr.append(arr_t)
#
# arr = [np.random.randint(1, 10, 6) for _ in range(6)]

sums = []
for i in range(0, 6 - 3+1):
    for j in range(0, 6 - 3+1):
        x = sum(arr[i][j:j + 3])
        y = arr[i + 1][j + 1]
        z = sum(arr[i + 2][j:j + 3])
        sums.append(x + y + z)

print(max(sums))

# res = []
#
# for x in range(0, 4):
#     for y in range(0, 4):
#         s = sum(arr[x][y:y + 3]) + arr[x + 1][y + 1] + sum(arr[x + 2][y:y + 3])
#         res.append(s)
#
# print(max(res))
