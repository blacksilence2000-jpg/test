def sum_list(nums):
    total = 0
    for n in nums:
        total += n
    return total

nums = [3, 7, 12, 5, 9] #testing list
print("the sum is:", sum_list(nums))
