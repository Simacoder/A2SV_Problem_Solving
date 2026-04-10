# Polycarp quest for maximum rest
import sys
input = sys.stdin.read().strip().split()

n = int(input[0])
a = list(map(int, input[1:]))

a = a + a

max_rest = 0
current = 0

for x in a:
    if x == 1:
        current += 1
        max_rest = max(max_rest, current)
    else:
        current = 0

print(min(max_rest, n))