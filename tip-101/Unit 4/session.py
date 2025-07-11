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



# The sliding window technique is an algorithmic technique often used to find a subarray or substring that meets certain criteria. 
# It works by initializing two pointers to point at the start and end of a ‘window’ or subsection of the string/array at a time. 
# The pointers are then incremented to slide the window and examine a different subarray or substring.
# Use the sliding window technique to solve the following problem:
# Write a function find_averages_of_subarrays() that takes in a list of integers nums and an integer k as parameters. 
# The function returns a list where each element in the average of each contiguous subarray of size k in nums where 1 ≤k ≤ len(nums)
# Plan: To find the average of each subarray, we will initialize a new list, and also window_sum as the sum of the first subarray in our nums list.
# Then, we will iterate through the list starting from after that first subarray, using nums[i-k] to subtract the first indice of the subarray and
# using nums[i] to add new values and create new subarrays and then take their average by dividing by k.

def find_averages_of_subarrays(k, nums):

    window_sum, newLst = sum(nums[0:k]), []
    
    for i in range(k, len(nums)): # k is stationary, i is dynamic and iterating
        newLst.append(window_sum / k) # k is the size of the subarray, 
        # It will always give us the first element of the current subarray we are on with i-k
        window_sum = window_sum - nums[i-k] + nums[i]

    newLst.append(window_sum/k)
    return newLst

nums = [1, 3, 2, 6, -1, 4, 1, 8, 2]
avg_lst = find_averages_of_subarrays(5, nums)

print(avg_lst)

# Write a function num_of_subarrays() that takes in a list of integers nums and two integers k and threshold as parameters.
# The function returns the number of subarrays of size k whose average is greater than or equal to threshold.
# Understand: We are asked to the number of subarrays with size k that have an average greater than or equal to the threshold given.
# Plan: We will initialize a window sum and count to keep track of the subarray totals and count of the subarrays. If our current window has an average
# that is greater than the threshold, then we will iterate the count. Starting from after that window, we will iterate and update the subarray to test
# each one.

def num_of_subarrays(lst, k, threshold):
    window_sum = sum(lst[0:k])
    count = 0

    if window_sum / k >= threshold:
        count += 1

    for i in range(k, len(lst)):
        window_sum = window_sum - lst[i-k] + lst[i]
        if window_sum / k >= threshold:
            count += 1
    return count



nums = [2,2,2,2,5,5,5,8]
count = num_of_subarrays(nums, 3, 4)
print(count)
    