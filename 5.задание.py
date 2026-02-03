nums = list(map(int, input().split()))

sorted_nums = sorted(nums)
median = sorted_nums[len(sorted_nums) // 2]
max_count = 0
mode = None

for i in range(len(nums)):
    seen_before = False
    for j in range(i):
        if nums[j] == nums[i]:
            seen_before = True
            break
    if not seen_before:
        count = 0
        for num in nums:
            if num == nums[i]:
                count += 1
        if count > max_count:
            max_count = count
            mode = nums[i]

print(median, mode)