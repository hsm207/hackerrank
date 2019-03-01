# Problem description: http://www.geeksforgeeks.org/count-number-of-ways-to-cover-a-distance/
from functools import lru_cache


@lru_cache(maxsize=None)
def ways_to_cover_distance(dist):
    if dist == 0:
        return 1
    elif dist < 0:
        return 0
    else:
        return ways_to_cover_distance(dist - 3) + ways_to_cover_distance(dist - 2) + ways_to_cover_distance(dist - 1)

print(ways_to_cover_distance(3))
print(ways_to_cover_distance(4))
print(ways_to_cover_distance(300))