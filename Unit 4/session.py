# Write a function sort_list_by_parity() that takes in an integer list nums as a parameter and moves all the even integers at the 
# beginning of the list followed by all the odd integers. The function returns any list that satisfies this condition.

# Understand: We want to sort/rearrange the list to where the even integers are at the front and all odd integers follow at the bak of the array
# Plan: We will use a two pointer strategy, one at start of list, another at the end of list, to compare odd and even numbers and swap them
# def sort_array_by_parity(nums):
#     left, right = 0, len(nums) - 1
#     while left < right:
#         if nums[left] % 2 == 0:
#             left += 1
#         else:
#             nums[left], nums[right] = nums[right], nums[left]
#             right -= 1
#     return nums
# nums = [3,1,2,4]
# nums2 = [0]
# nums3 = [3,2,33,3]
# nums4 = [3, 4, 5, 2, 22, 24, 42, 57, 102, 0, 0, 0, 3, 1, 2, 2, 2, 2]
# nums5 = [3, 1, 5, 7, 9, 2]
# print(sort_array_by_parity(nums5))
# print(sort_array_by_parity(nums))
# print(sort_array_by_parity(nums2))
# print(sort_array_by_parity(nums3))
# print(sort_array_by_parity(nums4))




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


# Write a function that takes in a string s and returns the length of the longest substring without repeating characters.

# Write a function that gets the length of the longest substring without any of the same characters (unique characters)
# We will use the sliding window technique in order to take unique substrings and find the max length of our substring. We will be using
# a set to easily track duplicates, then move to the next valid substring in the string. After the loop is finished, the max length of our window
# will give us our answer.

# def length_of_longest_substring(s):
#     l, longest = 0, 0 # Set left pointer at start, longest for longest subrstring results
#     seen = set() # Initialize a set
#     n = len(s) # variable for length of s
#     for r in range(n): # right pointer going through string with for loop
#         while s[r] in seen: # while right pointer character comes and stays in seen set
#             seen.remove(s[l]) # remove the left pointer character
#             l += 1 # Move left pointer up one
        
#         window = (r - l) + 1 # get length of current window
#         longest = max(longest, window) # Take the max of past windows, compared to the current window length
#         seen.add(s[r]) # Add the current right pointer character to seen
#     return longest # After the loop and we evaluate all possible unnique character windows, return the longest substring window length.

# s = "abcdeefghhhhh"
# count = length_of_longest_substring(s)
# print(count)

# s2 = "pwwwkew"
# count = length_of_longest_substring(s2)
# print(count)

"""
Problem Statement:

Developers working on a social media network app want to analyze user behavior.  
Each event log stores the user ID of the user that triggered the event.  

The team wants to analyze **consistent** subarrays of the logs, meaning:  
- A subarray is **consistent** if the **frequency of the most common element**  
  is **equal to** the **frequency of the least common element** in the subarray.  

Your task is to find the **maximum length of a consistent subarray**.

Example:
----------
Input:
    userEvent = [1, 2, 1, 3, 4, 2, 4, 3]
Output:
    8

Explanation:
    - The frequencies in the whole array are: 
      `{1:2, 2:2, 3:2, 4:2}`
    - The longest consistent subarray is `[1, 2, 1, 3, 4, 2, 4, 3]` with length **8**.
"""
# We are looking to find the length of the longest consistent subarray. Consistent in terms of all frequencies of the subarray are equal.
# We will use a sliding window strategy as we iterate through
# def max_length_consistent_subarray(userEvent):
#     pass

def reverse_list(lst):
    left = 0
    right = len(lst) - 1
    while left < right:
        lst[right], lst[left] = lst[left], lst[right]
        left += 1
        right -= 1
    return lst

nums_lst = [1,2,3,4,5]
nums_one = [2,5,7,8,8]
print(reverse_list(nums_one))


    