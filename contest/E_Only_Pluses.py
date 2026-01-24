t = int(input())

for _ in range(t):

    a, b, c = map(int, input().split())

    nums = [a, b, c]

    for _ in range(5):
        nums.sort()

        nums[0] += 1
    
    print(nums[0] * nums[1] * nums[2])

