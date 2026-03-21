# Prize fixed?
import sys

data = list(map(int, sys.stdin.buffer.read().split()))
n = data[0]


items = sorted(zip(data[2::2], data[1::2]))  
b_arr = [x[0] for x in items]
a_arr = [x[1] for x in items]

l, r = 0, n - 1
total = 0
cost = 0

while l <= r:
    if total >= b_arr[l]:
        cost += a_arr[l]
        total += a_arr[l]
        l += 1
    else:
        need = min(b_arr[l] - total, a_arr[r] if l != r else a_arr[l])
        cost += need * 2
        total += need
        if l == r:
            a_arr[l] -= need
        else:
            a_arr[r] -= need
            if a_arr[r] == 0:
                r -= 1

print(cost)