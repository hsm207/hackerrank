# Problem description: http://www.geeksforgeeks.org/dynamic-programming-set-7-coin-change/

def make_change(money, coins):
    if money < 0:
        return 0
    elif money == 0:
        return 1
    elif not coins:
        return 0
    else:
        return make_change(money - coins[-1], coins) + make_change(money, coins[:-1])


coins = [1, 2, 3]
money = 4
make_change(money, coins)