# chatloop 
import sys
input = sys.stdin.readline
from bisect import bisect_left

t = int(input())

for _ in range(t):
    n = int(input())
    a = map(int, input().split())
    b = map(int, input().split())

    position = {}
    for i , x in enumerate(b):
        position[x] = i
    
    seq = [position[x] for x in a]
    
    tails = []
    for val in seq:
        index = bisect_left(tails, val)
        if index == len(tails):
            tails.append(val)
        else:
            tails[index] = val
    print(n - len(tails))