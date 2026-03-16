# Chatloop
import sys
from bisect import bisect_left

input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    pos = {x: i for i, x in enumerate(b)}
    seq = [pos[x] for x in a]

    tails = []
    for x in seq:
        idx = bisect_left(tails, x)
        if idx == len(tails):
            tails.append(x)
        else:
            tails[idx] = x

    print(n - len(tails))
    sys.stdout.flush()