# Problem description: http://www.geeksforgeeks.org/dynamic-programming-set-31-optimal-strategy-for-a-game/

def optimal_strategy(coins):
    if len(coins) == 1:
        return coins[0]
    elif len(coins) == 2:
        return max(coins[0], coins[1])
    else:
        return max(coins[0] + min(optimal_strategy(coins[2:]),
                                  optimal_strategy(coins[1:-1])),
                   coins[-1] + min(optimal_strategy(coins[1:-1]),
                                   optimal_strategy(coins[:-2])))


coins = [8, 15, 3 , 7]
optimal_strategy(coins)
