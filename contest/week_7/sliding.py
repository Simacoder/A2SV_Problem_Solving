# sliding window
def max_sum(arr, k):
    n = len(arr)

    if n <= k:
        print("Invalid")
        return -1
    
    window_sum = sum(arr[: k])
    max_sum = window_sum

    for i in range(n - k):
        window_sum = window_sum - arr[i] + arr[i + 1]
        max_sum = max(window_sum, max_sum)
    
    return max_sum

arr = [5, 2, -1, 0, 3] # 5, 2, -1(maximum = 6), # 2, -1, 0 maximum = 1, to small
# -1, 0 , 3 maximum is 2 also too small, so the final answer is 6
k = 3
print(max_sum(arr, k))