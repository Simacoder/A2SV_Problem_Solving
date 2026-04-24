# helping ahmed in this harram strings
"""
import sys
input = sys.stdin.readline

n = int(input())

A,S, V = 0, 1, 2

if n == 1:
    print(3)
    exit()

dp = [[[0]* 3 for _ in range(3)] for _ in range(n + 1)]

for i in range(3):
    for j in range(3):
        if i != j:
            dp[2][i][j] = 1
for length in range(2, n):
    for last in range(3):
        for second_last in range(3):
            if dp[length][last][second_last] == 0:
                continue
            for nxt in range(3):
                if nxt == last:
                    continue
                if second_last == S and last == V and nxt == A:
                    continue
                dp[length + 1][nxt][last] += dp[length][last][second_last]

print(sum(sum(row) for row in dp[n]))
"""

n = int(input())

chars = ["A", "S", "V"]

def rec_count(pos, prev2, prev1):
    if pos == n:
        return 1
    
    total = 0
    for c in chars:
        if c == prev1:
            continue
        if prev2 == "S" and prev1 == "V" and c == "A":
            continue
        total += rec_count(pos + 1, prev1, c)
    
    return total

print(rec_count(0, -1, -1))