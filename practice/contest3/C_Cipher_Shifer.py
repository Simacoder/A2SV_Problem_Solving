# the deciphering king
import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    s = input().strip()

    answer = ""
    i = 0

    while i < n:
        c = s[i]
        answer += c
        i += 1

        while i < n and s[i] != c:
            i += 1
        i += 1
    
    print(answer)