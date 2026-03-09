# adding next to largest elite
import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    arr = sorted(map(int, input().split()))

    if arr[-1] > arr[0] + arr[1]:
        print("YES")
    else:
        print("NO")    

    