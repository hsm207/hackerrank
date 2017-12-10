import sys

n = int(input())
d = dict(input().split() for _ in range(n))

names = [n.strip() for n in sys.stdin.readlines()]

for name in names:
    if name in d:
        print('{}={}'.format(name, d[name]))
    else:
        print('Not found')

