# mountaining the peak
import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    h = list(map(int, input().split()))

    left_min_index = [0] * n
    left_min_index[0] = 0

    for i in range(1, n):
        if h[i] < h[left_min_index[i - 1]]:
            left_min_index[i] = i
        else:
            left_min_index[i] = left_min_index[i - 1]
    
    right_min_index = [0] * n
    right_min_index[n - 1] = n - 1

    for i in range(n - 2, -1, - 1):
        if h[i] < h[right_min_index[i + 1]]:
            right_min_index[i] = i
        else:
            right_min_index[i] = right_min_index[i + 1]
    
    found = False

    for j in range(n):
        if j == 0 or j == n - 1:
            continue

        i_index = left_min_index[j - 1]
        k_index = right_min_index[j + 1]

        #if i_index < j and k_index > j and h[i_index] < h[j] and h[k_index] < h[j]:
        if h[i_index] < h[j] and h[k_index] < h[j]:
            print("YES")
            print(i_index + 1, j + 1, k_index + 1)
            found = True
            break
    
    if not found:
        print("NO")



    
    