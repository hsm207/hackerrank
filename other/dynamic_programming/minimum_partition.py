# Problem description: http://www.geeksforgeeks.org/partition-a-set-into-two-subsets-such-that-the-difference-of-subset-sums-is-minimum/


def find_minimum_partition(array, set1, total_sum):
    # construct all possible values for set 1 from array
    if not array:

        sum_set1 = sum(set1)
        sum_set2 = total_sum - sum_set1
        return abs(sum_set1 - sum_set2)
    else:
        return min(find_minimum_partition(array[:-1], set1 + [array[-1]], total_sum),
                   find_minimum_partition(array[:-1], set1, total_sum))


arr = [3, 1, 4, 2, 2, 1]
print(find_minimum_partition(arr, [], sum(arr)))
