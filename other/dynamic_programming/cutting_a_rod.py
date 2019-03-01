cuts = []


def find_max_value(rod_size, prices, total_value):
    if rod_size < 0:
        return 0
    elif rod_size == 0:
        return total_value
    else:
        max_val = 0
        for cut, value in enumerate(prices, 1):
            max_val = max(max_val, find_max_value(rod_size - cut, prices, total_value + value))
        return max_val


prices = [1, 5, 8, 9, 10, 17, 17, 20]
find_max_value(8, prices, 0)
