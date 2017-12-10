import sys

n = int(input().strip())

b = bin(n)[2:]

max_consec_ones = max(len(g) for g in b.split('0'))

print(max_consec_ones)
