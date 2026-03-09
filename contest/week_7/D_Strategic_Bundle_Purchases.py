# purchases
import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    a.sort(reverse= True)
    b.sort()

    total = sum(a)
    discount = 0
    position = 0

    for x in b:
        if position + x > n:
            break
        discount += a[position + x - 1]
        position += x
    print(total - discount)
        