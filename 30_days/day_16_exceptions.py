import sys


S = 10

try:
    print(int(S))
except ValueError as e:
    print('Bad String')
