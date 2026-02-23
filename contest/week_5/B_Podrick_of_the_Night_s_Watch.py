import sys
from collections import defaultdict

input = sys.stdin.readline

n = int(input())
pair_count = defaultdict(int)

for _ in range(n):
    m = int(input())
    seen_today = set()
    
    for _ in range(m):
        parts = input().split()
        name = parts[0]
        hour = int(parts[1])
        seen_today.add((name, hour))
    
    for pair in seen_today:
        pair_count[pair] += 1

threshold = n * 0.8

for count in pair_count.values():
    if count >= threshold:
        print("YES")
        exit()

print("NO")