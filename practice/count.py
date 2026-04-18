# counting inutitive
nums = [1, 2, 2, 3, 4, 6]

count = {}

for num in nums:
    if num in count:
        count[num] += 1
    else:
        count[num] = 1
print(count)