# Mission team we are out of space?
import sys
input = sys.stdin.readline

n, d = map(int, input().split())
p = list(map(int, input().split()))

p.sort(reverse=True)

teams = 0
i = 0
j = n - 1

while i <= j:
    leader = p[i]
    need = d // leader + 1

    if i + (need - 1) <= j:
        teams += 1
        i += 1
        j -= (need - 1)
    else:
        break
    
print(teams)