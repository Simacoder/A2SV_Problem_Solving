# Polycarp's fav sequence
import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    b = list(map(int, input().split()))

    left, right = 0, n - 1
    arr = []

    while left <= right:
        if left == right:
            arr.append(b[left])
        else:
            arr.append(b[left])
            arr.append(b[right])
        left += 1
        right -= 1
    print(*arr)