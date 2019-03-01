# Problem description: https://jeremykun.com/2012/01/12/a-spoonful-of-python/
# recursive approach: http://www.mathcs.emory.edu/~cheung/Courses/323/Syllabus/DynProg/money-change.html

def coinChange(centsNeeded, coinValues):
    minCoins = [[0 for j in range(centsNeeded + 1)]
                for i in range(len(coinValues))]
    minCoins[0] = list(range(centsNeeded + 1))

    for i in range(1, len(coinValues)):
        for j in range(0, centsNeeded + 1):
            if j < coinValues[i]:
                # coin value being considered is greater than changed needed, so ignore it and use previous solution
                minCoins[i][j] = minCoins[i - 1][j]
            else:
                # if coin value can be considered as part of the solution, compare it to not included the coin (previous
                # solution) and effect of adding it
                minCoins[i][j] = min(minCoins[i - 1][j],
                                     1 + minCoins[i][j - coinValues[i]])

    for i in minCoins:
        print(i)
    return minCoins[-1][-1]


coinChange(10, [1, 5, 10, 50])

