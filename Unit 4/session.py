# Write a function sort_list_by_parity() that takes in an integer list nums as a parameter and moves all the even integers at the 
# beginning of the list followed by all the odd integers. The function returns any list that satisfies this condition.

# Understand: We want to sort/rearrange the list to where the even integers are at the front and all odd integers follow at the bak of the array
# Plan: We will use a two pointer strategy, one at start of list, another at the end of list, to compare odd and even numbers and swap them
def sort_array_by_parity(nums):
    left, right = 0, len(nums) - 1
    while left < right:
        if nums[left] % 2 == 0:
            left += 1
        else:
            nums[left], nums[right] = nums[right], nums[left]
            right -= 1
    return nums
nums = [3,1,2,4]
nums2 = [0]
nums3 = [3,2,33,3]
nums4 = [3, 4, 5, 2, 22, 24, 42, 57, 102, 0, 0, 0, 3, 1, 2, 2, 2, 2]
nums5 = [3, 1, 5, 7, 9, 2]
print(sort_array_by_parity(nums5))
print(sort_array_by_parity(nums))
print(sort_array_by_parity(nums2))
print(sort_array_by_parity(nums3))
print(sort_array_by_parity(nums4))




    # left, right = 0, len(nums) - 1 # Initialize two pointers, one at starting index, one at the last index
    # while left < right: # While the pointers do not meet, run this code
    #     if nums[left] % 2 == 0: # If left pointer is even, run this code
    #         left += 1 # Iterate left to a new index
    #     else: # Otherwise its odd
    #         if nums[right] % 2 == 0: # If right is even, run this code
    #             nums[left], nums[right] = nums[right], nums[left] # Swap placements of the values so that the even is in the front
    #             left += 1 # Iterate the left to a new index
    #             right -= 1 # Iterate the right to a new index
    #         else:
    #             right -= 1 # Else we will keep moving the right until we touch the left and theres no odd numbers OR uuntil we find an odd number.
    # return nums # After the while loop return the rearranged nums.