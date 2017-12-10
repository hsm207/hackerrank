#!/bin/python3

import sys

n = int(3)
a = list(map(int, [3, 2, 1]))
# Write Your Code Here

numberOfSwaps = 0
for i in range(n):

    for j in range(i, n - 1):
        if a[i] > a[j + 1]:
            numberOfSwaps += 1
            a[i], a[j + 1] = a[j + 1], a[i]

print('Array is sorted in {} swaps.'.format(numberOfSwaps))
print('First Element: {}'.format(a[0]))
print('Last Element: {}'.format(a[-1]))
