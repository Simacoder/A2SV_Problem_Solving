# The socialist state: the welfate goveernance
import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
q = int(input())

events = []
for _ in range(q):
    line = list(map(int, input().split()))
    events.append(line)

last_val = a[:]
last_time = [0] * n

suffix_max = [0] * (q + 2)

for t, event in enumerate(events, 1):
    if event[0] == 1:
        p, x = event[1] - 1, event[2]
        last_val[p]  = x
        last_time[p] = t

for t, event in enumerate(events, 1):
    if event[0] == 2:
        suffix_max[t] = event[1]

for t in range(q, 0, -1):
    suffix_max[t] = max(suffix_max[t], suffix_max[t + 1])

output = []
for i in range(n):
    val = max(last_val[i], suffix_max[last_time[i] + 1])
    output.append(val)
sys.stdout.write(" ".join(map(str, output)) + "\n")
