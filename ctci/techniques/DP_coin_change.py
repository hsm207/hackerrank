from functools import lru_cache


# recursive version
# source: http://algorithmist.com/index.php/Coin_Change
@lru_cache(maxsize=None)
def make_change(coins, amount):
    if amount < 0 or not coins:
        return 0
    elif amount == 0:
        return 1
    else:
        return make_change(coins, amount - coins[-1]) + make_change(coins[:-1], amount)


# dynamic programming version
def make_change(coins, n):
    # initialize the table
    lookup_table = [[0 for column in range(n + 1)] for row in range(len(coins))]

    # populate the base cases
    coin_val = coins[0]

    # if the value of the smallest coin evenly divides the dollar amount to change,
    # then there is exactly 1 way to make the change
    for money_val, _ in enumerate(lookup_table[0]):
        lookup_table[0][money_val] = 1 if money_val % coin_val == 0 else 0

    # there is exactly 1 way to use any combination of coins to get $0
    for coin_val, _ in enumerate(lookup_table[:]):
        lookup_table[coin_val][0] = 1

    # fill the table
    for i in range(1, len(coins)):
        for money_val in range(1, n + 1):
            if money_val < coins[i]:
                lookup_table[i][money_val] = lookup_table[i - 1][money_val]
            else:
                lookup_table[i][money_val] = lookup_table[i - 1][money_val] + lookup_table[i][money_val - coins[i]]

    return lookup_table[-1][-1]


n = 12
coins = [1, 2, 5]
make_change(sorted(coins), n)
