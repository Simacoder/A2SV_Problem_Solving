# huge council 
import sys
input = sys.stdin.readline
from collections import Counter

n = int(input())
s = input().strip()

freq = {}

for c in s:
    freq[c] = freq.get(c, 0) + 1

distinct = len(freq)

if distinct == 1:
    print("Yes")
elif distinct == 2 and min(freq.values()) >= 2:
    print("Yes")
elif any(v >= 2 for v in freq.values()):
    print("Yes")
else:
    print("No")