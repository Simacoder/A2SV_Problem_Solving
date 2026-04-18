# two pointers of two sum
def two_sum(nums, target):
    left, right = 0, len(nums) -1

    while left < right:
        sum_me = nums[left] + nums[right]
        if sum_me < target:
            left += 1
        elif sum_me > target:
            right -= 1
        else:
            sum_me == target
            return [left, right]
    return []

nums = [-5, -2, 3, 4, 6]
target = 7
print(two_sum(nums, target)) 