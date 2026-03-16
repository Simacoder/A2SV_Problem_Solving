# numbered card 
import sys
input = sys.stdin.readline()

t = int(input())

for _ in range(t):
    n, m = map(int, input().split())

    arr = []
    for _ in range(n):
        arr.extend(map(int, input().split()))
    
    N = n * m

    if N ==  1:
        print(-1)
        continue

    b = None

    for shift in [m, 1, N - m, N - 1]:
        if shift <= 0 or shift >= N:
            continue
        candi = arr[shift] + arr[:shift]
        if all(candi[i] != arr[i] for i in range(N)):
            b = candi
            break

    if b is None:
        for shift in range(2, N):
            candi = arr[shift:] + arr[:shift]
            if all(candi[i] != arr[i] for i in range(N)):
                b = candi
                break
    if b is None:
        print(-1)
    else:
        indexx = 0
        for i in range(n):
            print(*b[indexx:indexx + m])
            indexx += m
        