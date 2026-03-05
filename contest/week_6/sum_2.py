# testing this
def sum_two(arr, target):
    n = len(arr)
    for i in range(n):
        for j in range(i + 1, n):
            if arr[i] + arr[j] == target:
                return True
            else:
                return False
    return False

arr = [0, -1, 2, -3, 1]
target = -2

print(sum_two(arr,target))