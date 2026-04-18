# mark the janitor
import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    answer = 0

    found = False

    for i in range(n - 1):
        if a[i] > 0:
            answer += a[i]
            found = True
        elif found:
            answer += 1
    print(answer)