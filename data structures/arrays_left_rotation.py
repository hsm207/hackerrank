def array_left_rotation(a, n, k):
    from collections import deque
    b = deque(a)
    b.rotate(-k)
    return b


n, k = map(int, input().strip().split(' '))
a = list(map(int, input().strip().split(' ')))
answer = array_left_rotation(a, n, k);
print(*answer, sep=' ')