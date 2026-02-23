# sequence of the dice
import sys
input = sys.stdin.readline

t = int(input())
INF = 10**18

adj = [[] for _ in range(7)]
for u in range(1, 7):
    for v in range(1, 7):
        if u != v and u + v != 7:
            adj[u].append(v)

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    
    dp = [(a[0] != v) for v in range(7)]
    
    for i in range(1, n):
        new = [INF]*7
        for v in range(1, 7):
            new[v] = min(dp[u] for u in adj[v]) + (a[i] != v)
        dp = new
    
    print(int(min(dp[1:])))  
