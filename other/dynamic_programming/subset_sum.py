# Problem description: http://www.geeksforgeeks.org/dynamic-programming-subset-sum-problem/

def find_subset_with_sum1(source_set, subset, target_sum):
    if not source_set:
        subset_exist = sum(subset) == target_sum

        if subset_exist:
            print(subset)

        return subset_exist

    else:
        return find_subset_with_sum1(source_set[:-1], subset + [source_set[-1]], target_sum) \
               or find_subset_with_sum1(source_set[:-1], subset, target_sum)


def find_subset_with_sum2(source_set, subset, target_sum):
    print(subset)
    if  target_sum == 0 or  not source_set:
        subset_exist = 0 == target_sum

        if subset_exist:
            print(subset)

        return subset_exist

    else:
        return find_subset_with_sum2(source_set[:-1], subset + [source_set[-1]], target_sum - source_set[-1]) \
               or find_subset_with_sum2(source_set[:-1], subset, target_sum)


given_set = [3, 34, 4, 12, 5, 2]
given_sum = 9
find_subset_with_sum2(given_set, [], given_sum)
