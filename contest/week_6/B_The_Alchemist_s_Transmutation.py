# The alchemist test of energy for transmutation 
import sys
input = sys.stdin.readline 

t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    x = int(input())

    if min(a) <= x <= max(a):
        print("YES")
    else:
        print("NO")