# how many books
import sys
input = sys.stdin.readline

n, t = map(int, input().split())
arr = list(map(int, input().split()))

left = 0
s = 0
answer = 0

for right in range(n):
    s += arr[right]

    while s > t:
        s -= arr[left]
        left += 1
    answer = max(answer, right - left + 1)
print(answer)