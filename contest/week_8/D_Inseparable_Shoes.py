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

        for k in range(i, j - 1):
            p[k] = k + 2
        p[j - 1] = i + 1
        i = j
    
    if not possible:
        print(-1)
    else:
        print(*p)
