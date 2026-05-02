# another one Kidus trying to be za Kidus
import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    h = list(map(int, input().split()))
    d = list(map(int, input().split()))

    arr =sorted(zip(d, h))

    def can(X):
        current = 0
        for deadline, health in arr:
            current += (health + X - 1) // X
            if current > deadline:
                return False
        return True
    
    low, high = 1, max(h)
    answer = high

    while low <= high:
        mid = (low + high) // 2
        if can(mid):
            answer = mid
            high = mid - 1
        else:
            low = mid + 1
        
    print(answer)