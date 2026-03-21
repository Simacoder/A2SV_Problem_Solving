# numbered card 
import sys
input = sys.stdin.readline


t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    a = []
    for _ in range(n):
        a.append(list(map(int, input().split())))
    if n * m == 1:
        print(-1)
        continue
    for i in range(n):
        row = [a[(i+1)%n][(j+1)%m] for j in range(m)]
        print(*row)


