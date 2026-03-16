# A business plan or a gambling plan
import sys
import heapq
from itertools import groupby
input = sys.stdin.buffer.read


data = input().split()
indexx = 0

output = []

t = int(data[indexx]); indexx +=1

for _ in range(t):
    n , k = int(data[indexx]), int(data[indexx + 1]); indexx += 2

    brand_sum = [0] * (k + 1)

    for _ in range(k):
        b , c = int(data[indexx]), int(data[indexx + 1]); indexx += 2
        brand_sum[b] +=  c

    vals = [v for v in brand_sum if v > 0]
    m = len(vals)

    if m <= n:
        output.append(sum(vals))
    else:
        if n > m - n:
            vals.sort()
            output.append(sum(vals[m - n:]))
        else:
            heap =  vals[:n]
            heapq.heapify(heap)
            heap_min = heap[0]
            total = sum(heap)
            for v in vals[n:]:
                if v > heap_min:
                    total += v - heap_min
                    heapq.heapreplace(heap, v)
                    heap_min = heap[0]
            output.append(total)

sys.stdout.write('\n'.join(map(str, output)) + '\n')