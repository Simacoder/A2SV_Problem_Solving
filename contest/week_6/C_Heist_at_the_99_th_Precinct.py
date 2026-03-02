# Team Dagi , can Dagi's strategy win?
import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    max_val = max(a)

    count_max =a.count(max_val)
    rest = n - count_max

    if count_max % 2 == 0 and rest % 2 == 0:
        print("NO")
    else:
        print("YES")



