# an optimistic student as they look for max possible scores
import sys 
input = sys.stdin.readline

n, m = map(int, input().split())
students = [input() for _ in range(n)]
points = list(map(int, input().split()))

total = 0

for j in range(m):
    count = [0] * 5

    for k in range(n):
        count[ord(students[k][j]) - ord('A')] += 1

    total += max(count) * points[j]

print(total)