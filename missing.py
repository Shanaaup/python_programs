def find_missing_number(nums, n):
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(nums)
    return expected_sum - actual_sum

# Input
n = int(input())
nums = list(map(int, input().split()))

# Output
print(find_missing_number(nums, n))