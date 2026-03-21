# polycarp?? sound familiar
import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    s = input().strip()
    n = len(s)

    working = set()

    i = 0
    while i < n:
        j = i
        while j < n and s[j] == s[i]:
            j += 1
        
        long = j - i

        if long % 2 == 1:
            working.add(s[i])
        
        i = j
    print("".join(sorted(working)))

