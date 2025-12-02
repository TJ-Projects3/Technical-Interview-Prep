# Given an array of integers (nums) and an integer (target), determine if
# there are two numbers in the array that add up to the target.
# Return True if such a pair exists, otherwise return False.
# You may not assume that each input would have at least one solution,
# and you may not use the same element twice.

# Input: nums = [3, 1, 7, 9, 2], target = 10
# 10 - 3 = 7
# 10 - 7 = 3

# We are finding two numbers that aren't the same index that add up to the target
# Return their index
# Brute force: O(n^2) 
# O(1) lookup
# for i, val in enumerate(nums):
    # Check dictionary for target-val
        # return [dict[target-val], i]
    # Add val as key and index as the value

def two_sum(nums, target):
    count = {}

    for i, val in enumerate(nums): # O(n)
        if target - val in count:
            return [count[target-val], i]
        count[val] = i # O(n)

nums_test = [3, 1, 7, 9, 2]
target_test = 10
print(two_sum(nums_test, target_test))
            