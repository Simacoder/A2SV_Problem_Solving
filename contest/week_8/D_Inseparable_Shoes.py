# a pair of Shoes
import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    s = list(map(int, input().split()))

    p = [0] * n
    possible = True
    i = 0

    while i < n:
        j = i
        while j < n and s[j] == s[i]:
            j += 1

        if j - i == 1:
            possible = False
            break

        
        p[i] = j
        for k in range(i + 1, j):
            p[k] = k

        i = j

    if not possible:
        print(-1)
    else:
        print(*p)