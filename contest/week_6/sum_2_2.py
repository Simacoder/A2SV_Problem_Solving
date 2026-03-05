# using two pointer
def sum_two(arr, target):
    left = 0
    right = len(arr) - 1

    while left < right:
        sum_is = arr[left]  + arr[right]
        if sum_is == target:
            return arr[left], arr[right]
        elif sum_is < target:
            left += 1
        else:
            right -= 1
    return False

arr = [0, -1, 2, -3, 1]
target = -1

print(sum_two(arr, target))