# Problem description: https://www.hackerrank.com/challenges/ctci-merge-sort/problem
def countInversions(a):
    if len(a) < 2:
        # array size of less than two means 1..can't do swaps!
        return 0
    else:
        count = 0
        mid_index = (len(a) // 2)  # divide into two array
        left_array = a[0:mid_index]  # take first half of array
        right_array = a[mid_index:]  # take second half of array
        count += countInversions(left_array)  # get inversion count from left array
        count += countInversions(right_array)  # get inversion count from right array
        count += merge(left_array, right_array, a)  # get inversion count from the main array
        return count


def merge(left_array, right_array, a):
    left_start = 0
    left_end = len(left_array)
    right_start = 0
    right_end = len(right_array)
    count = 0
    index = 0  # index for new array that both left and right array will merge into

    # the merge algorithm
    while left_start < left_end and right_start < right_end:
        if left_array[left_start] <= right_array[right_start]:
            a[index] = left_array[left_start]
            left_start += 1
        elif left_array[left_start] > right_array[right_start]:
            count += left_end - left_start  # count increment by how many item right array skips over in left array.
            a[index] = right_array[right_start]
            right_start += 1
        index += 1

    if left_start < left_end:  # this adds the remainder elements not compared in the merge
        while index < len(a):
            a[index] = left_array[left_start]
            index += 1
            left_start += 1
    elif right_start < right_end:
        while index < len(a):
            a[index] = right_array[right_start]
            index += 1
            right_start += 1
    return count


sample_input = [2, 1, 3, 1, 2]
countInversions(sample_input)
