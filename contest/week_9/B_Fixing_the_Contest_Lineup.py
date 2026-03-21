# can the contest lineup be fix?
import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    i = 0
    j = 0
    ops = 0

    while i < n and j < n:
        if a[i] <= b[j]:
            i += 1
            j += 1
        else:
            ops += 1
            j += 1
    print(ops)