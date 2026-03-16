# Prize fixed?
import sys
input = sys.stdin.readline

n = int(input())
items = []

for _ in range(n):
    a, b = map(int, input().split())
    items.append([a, b])

items.sort(key=lambda x: x[1])

left, right =0, n - 1
bought = 0
cost = 0

while left <= right:
    if bought >= items[left][1]:
        cost += items[left][0]
        bought += items[left][0]
        left += 1
    else:
        need = min(items[right][0], items[left][1] - bought)
        cost += need * 2
        bought += need
        items[right][0] -= need

        if items[right][0] == 0:
            right -= 1
    print(cost)