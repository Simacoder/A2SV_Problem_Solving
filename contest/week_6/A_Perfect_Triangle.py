# A perfect triangel in aperfect world
import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    a. sort()

    answer = float('inf')

    for i in range(n - 2):
        answer = min(answer, a[i + 2] - a[i])
    print(answer)