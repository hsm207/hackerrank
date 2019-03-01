from functools import lru_cache


def findFlavour(money, flavourCost):
    i = 0
    while i < len(flavourCost):
        if (money - flavourCost[i]) in flavourCost and flavourCost.index(money - flavourCost[i]) != i:
            temp = flavourCost[i]
            flavourCost[i] = -1
            if flavourCost.index(money - temp) > i:
                return i + 1, flavourCost.index(money - temp) + 1
            else:
                return flavourCost.index(money - temp) + 1, i + 1
        i += 1


#print(findFlavour(10, [1, 4, 5, 3, 2]))


# non-binary search
def get_flavours(money, flavours):
    map = {}
    for pos in range(len(flavours)):
        cost = flavours[pos]
        compliment = money - cost
        if compliment in map:
            return (flavours.index(compliment) + 1, pos + 1)
        else:
            map[cost] = compliment


# using binary search
class IceCreamSolution:
    def __init__(self, cost):
        # store the list of costs as a list of tuples: (cost_for_ice_cream_i, index_of_ice_cream_i + 1)
        self.costs = sorted((cost, i + 1) for i, cost in enumerate(cost))

    @lru_cache(maxsize=None)
    def binary_search(self, costs, value, start_index, end_index):
        middle_index = (start_index + end_index) // 2
        middle_cost = costs[middle_index]

        if start_index > end_index:
            return None
        elif value > middle_cost[0]:
            return self.binary_search(costs, value, middle_index + 1, end_index)
        elif value < middle_cost[0]:
            return self.binary_search(costs, value, start_index, middle_index - 1)
        else:
            return middle_cost

    def find_combination(self, money):
        for cost in self.costs:
            copy_costs = list(self.costs)
            copy_costs.remove(cost)

            money_complement = money - cost[0]
            cost_complement = self.binary_search(tuple(copy_costs), money_complement, 0, len(copy_costs) - 1)
            if cost_complement:
                return sorted((cost[1], cost_complement[1]))


#print(get_flavours(4, [1, 4, 5, 3, 2]))
sample_input = [5, 75, 25]
sample_money = 100
x = IceCreamSolution(sample_input)
x.find_combination(sample_money)
