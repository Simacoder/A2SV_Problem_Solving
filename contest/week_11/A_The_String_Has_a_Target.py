# the string with a trget
import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    s = input().strip()

    m = min(s)

    i = s.rfind(m)

    answer = s[i] + s[:i] + s[i + 1:]
    print(answer)