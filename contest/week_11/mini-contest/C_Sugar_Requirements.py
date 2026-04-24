from bisect import bisect_left
import sys
input = sys.stdin.readline

t =  int(input())
for _ in range(t):
    n,q = map(int, input().split())
    a = list(map(int, input().split()))
    
    a.sort(reverse=True)
    prefix = [0] * n
    prefix[0] = a[0]
    for i in range(1, n):
        prefix[i] = prefix[i-1] + a[i]
    # print(a)
    # print(prefix)
    
    res = []
    for _ in range(q):
        num = int(input())
        
        if num > prefix[-1]:
            res.append(-1)
            continue
        idx = bisect_left(prefix, num)
        res.append(idx + 1)
    for i in res:
        print(i)