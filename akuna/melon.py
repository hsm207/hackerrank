def melon_count_helper(boxes, melons, count):
    if not boxes:
        return count
    elif melons[-1] <= boxes[-1]:
        return max(melon_count_helper(boxes[:-1], melons[:-1], count + 1),
                   melon_count_helper(boxes[:-1], melons, count))
    else:
        return melon_count_helper(boxes[:-1], melons, count)


def melon_count(boxes, melons):
    return melon_count_helper(boxes, melons, 0)


melon_count([1, 2, 1, 2], [3, 3, 2, 1])
melon_count([2, 1, 2, 2], [3, 2, 3, 2])

from functools import lru_cache
