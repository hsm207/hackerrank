from math import sqrt


def distance_between_points(point1, point2):
    x1, y1 = point1
    x2, y2 = point2

    return sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


def count_rocks_helper(ribbon_length, rocks, selected_rocks):
    # stop recursing when there are no rocks left
    if not rocks:
        return len(selected_rocks[:-1])
    # stop recursing when there is not enough ribbon to surround the selected rocks
    elif selected_rocks and distance_between_points(selected_rocks[0], selected_rocks[-1]) > ribbon_length:
        return len(selected_rocks[:-1])
    else:
        max_rocks = 0
        for rock in rocks:
            candidate_rocks = list(rocks)
            candidate_rocks.remove(rock)

            max_rocks = max(max_rocks, count_rocks_helper(ribbon_length - distance_between_points(selected_rocks[-1],
                                                                                                  rock),
                                                          candidate_rocks, selected_rocks + [rock]))
        return max_rocks


def count_rocks(ribbon_length, rocks):
    results = []
    for rock in rocks:
        candidate_rocks = list(rocks)
        candidate_rocks.remove(rock)
        results.append(count_rocks_helper(ribbon_length, candidate_rocks, [rock]))

    return max(results)


ribbon_length = 10.0
rocks = [[0, 0], [0, 3], [3, 3]]

count_rocks(ribbon_length, rocks)
