def find_equal_partition(origin_set, set1, set2):
    if not origin_set:
        exists = sum(set1) == sum(set2)
        if exists:
            print(set1)
            print(set2)
        return exists
    else:
        return find_equal_partition(origin_set[:-1], set1 + [origin_set[-1]], set2) \
               or find_equal_partition(origin_set[:-1], set1, set2 + [origin_set[-1]])


given_set = [3, 1, 5, 9, 12]
find_equal_partition(given_set, [], [])
