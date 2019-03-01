# Problem description: http://www.geeksforgeeks.org/knapsack-problem/
from functools import lru_cache

@lru_cache(maxsize=None)
def knapsack(item_values, item_weights, capacity):
    # return 0 when no items are left
    if not item_values:
        return 0
    # return 0 when you have no more capacity to take on items
    elif capacity <= 0:
        return 0
    # skip the item if its weight is greater than current capacity
    elif item_weights[-1] > capacity:
        return knapsack(item_values[:-1], item_weights[:-1], capacity)
    else:
        # max(try including item in the sack, try not including the item in the sack)
        return max(item_values[-1] + knapsack(item_values[:-1], item_weights[:-1], capacity - item_weights[-1]),
                   knapsack(item_values[:-1], item_weights[:-1], capacity))

val = (60, 100, 120)
wt = (10, 20, 30)
W = 50
n = len(val)

knapsack(val, wt, W)