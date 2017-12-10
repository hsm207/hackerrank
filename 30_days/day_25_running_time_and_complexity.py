# from https://www.hackerrank.com/challenges/30-running-time-and-complexity/forum/comments/171606
import math

for _ in range(int(input())):
    n = int(input())
    sqrt = int(math.ceil(math.sqrt(n)))

    if n == 1:
        print("Not prime")
    elif n == 2:
        print("Prime")
    else:
        for i in range(2, sqrt + 1):
            if n % i == 0:
                print("Not prime")
                break
        else:
            print("Prime")