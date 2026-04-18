# All lengths substraction 
t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    for k in range(n, 0, -1):
        for i in range(n - k + 1):
            if min(a[i:i+k]) > 0:
                for j in range(i, i + k):
                    a[j] -= 1
                break
        else:
            print("NO")
            break
    else:
        print("YES")