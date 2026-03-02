import sys
raw_input = sys.stdin.readline
n = int(raw_input())

p = 1 << (n - 1)
q = (1 << n) - 1

print("%d/%d" % (p, q))