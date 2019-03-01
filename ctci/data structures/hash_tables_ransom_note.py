# Problem description: https://www.hackerrank.com/challenges/ctci-ransom-note/problem
from collections import Counter

def ransom_note(magazine, ransom):
    mag_counter = Counter(magazine)
    ransom_counter = Counter(ransom)

    return not ransom_counter - mag_counter


m, n = 6, 4
magazine = 'give me one grand today night'.split()
ransom = 'give one grand today'.split()

answer = ransom_note(magazine, ransom)
if (answer):
    print("Yes")
else:
    print("No")

