# Denel the equalize
import sys
input = sys.stdin.buffer.read

data = input().split()

indexx = 0
t = int(data[indexx]); indexx += 1
output = []

for _ in range(t):
    n = int(data[indexx]); indexx += 1
    a = [int(data[indexx +1]) for i in range(n)]; indexx += n

    uniqq = sorted(set(a))
    m = len(uniqq)

    events = []
    for u in uniqq:
        events.append((u + 1, 1))
        events.append((u + n + 1, -1))
    events.sort()

    answer = cur = 0

    for val, delta in events:
        cur += delta
        if delta == 1:
            answer = max(answer, min(cur, m))
output.append(answer)

sys.stdout.write('\n'.join(map(str, output)) + '\n')

