# The competition is the life
import sys
from collections import defaultdict
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    u = list(map(int, input().split()))
    s = list(map(int, input().split()))

    
    groups = defaultdict(list)
    for grp, skill in zip(u, s):
        groups[grp].append(skill)

    
    prefix_groups = {}
    for grp in groups:
        groups[grp].sort(reverse=True)
        prefix = []
        total = 0
        for skill in groups[grp]:
            total += skill
            prefix.append(total)
        prefix_groups[grp] = prefix

    ans = [0] * n

    
    for prefix in prefix_groups.values():
        m = len(prefix)
        for k in range(1, m+1):
            full_teams = m // k
            if full_teams > 0:
                ans[k-1] += prefix[full_teams * k - 1]

    print(*ans)