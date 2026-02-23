k, n, w = map(int, input().split())

total_of_cost = k * w * (w + 1) // 2

credit = total_of_cost - n
print(max(0, credit))