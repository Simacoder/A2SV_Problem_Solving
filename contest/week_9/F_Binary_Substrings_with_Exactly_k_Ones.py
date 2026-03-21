# binary string with exactly k one
import sys
from collections import defaultdict
input = sys.stdin.readline

k = int(input())
s = input().strip()

freq = defaultdict(int)
freq[0] = 1
count_ones = 0
answer = 0

for c in s:
    if c == '1':
        count_ones += 1
    answer += freq[count_ones - k]
    freq[count_ones] += 1

print(answer)