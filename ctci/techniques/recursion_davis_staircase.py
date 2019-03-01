from functools import lru_cache

@lru_cache(maxsize=None)
def number_of_ways_to_climb(stair_height):
    if stair_height == 0:
        return 1
    elif stair_height < 0:
        return 0
    else:
        return number_of_ways_to_climb(stair_height - 1) + number_of_ways_to_climb(
            stair_height - 2) + number_of_ways_to_climb(stair_height - 3)


# def number_of_ways_to_climb(stair_height):
#     steps = [1, 2, 3]
#     lookup_table = [[0 for column in range(0, stair_height + 1)] for row in range(len(steps))]
#
#     # populate base case
#     for stair_height, _ in enumerate(lookup_table[0]):
#         lookup_table[0][stair_height] = 1
#
#     for step_size, _ in enumerate(steps):
#         lookup_table[step_size][0] = 1
#
#     # fill the table
#     for step_index, step_value in enumerate(steps[1:], 1):
#         for stair_height_value, _ in enumerate(lookup_table[0][1:], 1):
#             if step_value > stair_height_value:
#                 lookup_table[step_index][stair_height_value] = lookup_table[step_index - 1][stair_height_value]
#             else:
#                 lookup_table[step_index][stair_height_value] = lookup_table[step_index - 1][stair_height_value - 1] \
#                                                                + lookup_table[step_index ][stair_height_value - 1]
#
#     return lookup_table[-1][-1]


sample_inputs = [3, 7]

for s in sample_inputs:
    print(number_of_ways_to_climb(s))
