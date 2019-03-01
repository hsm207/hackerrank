# Problem description: https://www.hackerrank.com/challenges/ctci-making-anagrams/problem
from collections import Counter


def number_needed(a, b):
    a_count = Counter(a)
    b_count = Counter(b)

    # compute the count difference for each character in a and b
    # if the difference is not 0, then we need to delete that character

    a_count.subtract(b_count)

    return sum(abs(i) for i in a_count.values())


a = 'cde'
b = 'abc'

print(number_needed(a, b))
