# Can you survive and kill all n monsters without letting them reach your character?
# we will never know 
import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    x = list(map(int, input().split()))

    monsters = sorted((abs(x[i]), a[i]) for i in range(n))

    total = 0
    ok = True

    for dist, hp in monsters:
        total += hp

        if total > k * dist:
            ok = False

            break
    
    print("YES" if ok else "NO")
