# selective connection

import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))


    need = 1
    even = k // 2
    i = 0

    for evn in range(even):
        found = False

        while i < n:
            if a[i] == need:
                need += 1
                found = True
            i += 1
            if found:
                break

        while i < n and found:
            if a[i] == need:
                need += 1
            else:
                break
    print(need)

   

