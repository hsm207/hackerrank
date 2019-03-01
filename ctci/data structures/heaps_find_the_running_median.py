# Problem description: https://www.hackerrank.com/challenges/ctci-find-the-running-median/problem

import sys
import bisect
import heapq
import math

sample_inputs = [12, 4, 5, 3, 8, 7]

# using bisect
sorted_inputs = []

for i in range(len(sample_inputs)):

    bisect.insort_left(sorted_inputs, sample_inputs[i])
    n = len(sorted_inputs)
    if n % 2 != 0:
        median = float(sorted_inputs[math.floor(n / 2)])
        print(median)
    else:
        median = float((sorted_inputs[n // 2 - 1] + sorted_inputs[n // 2]) / 2)
        print(median)

# using heapq
# key idea: first element in a heapq is always the smallest element in that list
# heap max will store the lower half of the sequence
heap_max = []
# heap_min will store the upper half of the sequence
heap_min = []

for a_i in sample_inputs:

    # store the first input into heap_max
    if not heap_max:
        heapq.heappush(heap_max, -a_i)
    # if the input is smaller than the smallest lower half, put it there
    elif a_i < abs(heap_max[0]):
        heapq.heappush(heap_max, -a_i)
    # otherwise put it in the upper half
    else:
        heapq.heappush(heap_min, a_i)

    # this part ensures the difference in length is never greater than 1
    if len(heap_min) - len(heap_max) > 1:
        heapq.heappush(heap_max, -heapq.heappop(heap_min))
    elif len(heap_max) - len(heap_min) > 1:
        heapq.heappush(heap_min, -heapq.heappop(heap_max))

    if len(heap_max) == len(heap_min):
        median = (-heap_max[0] + heap_min[0]) / 2.0


    elif len(heap_max) > len(heap_min):
        median = -heap_max[0]

    else:
        median = heap_min[0]

    print(float(median))
