# lexical order
import sys
input = sys.stdin.readline

n = int(input())

a = list(map(int, input().split()))
is_even = any(x % 2 == 0 for x in a)
is_odd = any(x % 2 == 1 for x in a)

if is_even and is_odd:
    a.sort()
print(" ".join(map(str, a)))
    