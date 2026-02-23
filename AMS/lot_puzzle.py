import sys

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))

# reduces to residues
a = [x % 100 for x in a]

count = 0

for mask in range(1, 1 << n):
    s = 0
    for i in range(n):
        if mask & (1 << i):
            s += a[i]
        
    if s % 100 == 0:
        count += 1
print(count)
