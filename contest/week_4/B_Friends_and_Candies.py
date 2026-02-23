# Candies issue with distribtuion 
import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    array_list = list(map(int, input().split()))

    s = sum(array_list)

    if s % n != 0:
        print(-1)
        continue
    
    target = s // n

    k = sum(1 for y in array_list if y > target)
    print(k)

