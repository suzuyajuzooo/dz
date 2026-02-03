numbers = list(map(float, input().split()))
avg = sum(numbers) / len(numbers)
sorted_nums = sorted(numbers)
n = len(sorted_nums)
if n % 2 == 1:
    median = sorted_nums[n // 2]
else:
    median = (sorted_nums[n // 2 - 1] + sorted_nums[n // 2]) / 2
print(f"{avg} {median}")