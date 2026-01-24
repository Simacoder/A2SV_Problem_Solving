k , n, w = map(int, input().split())

cost_total = k * w * (w + 1) // 2

borrowed = cost_total - n
print(max(0, borrowed))


