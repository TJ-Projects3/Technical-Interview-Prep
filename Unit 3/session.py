# Write a function swap_ends() that accepts a string my_str as a parameter and 
# returns a new string where the first and last characters from my_str are swapped.
def swap_ends(my_str):
    str = ""
    for i in range(len(my_str)):
        if (i == 0):
            str += my_str[len(my_str) - 1]
        elif(i == len(my_str) - 1):
            str += my_str[0]
        else:
            str += my_str[i]
    return str

stringOne = "gonow"
print(swap_ends(stringOne))

# Write a function is_pangram() that takes in a string my_str as a parameter
#  and returns True if the string is a pangram and False if not.
#  A pangram is a sentence containing every letter in the English alphabet.
def is_pangram(my_str):
    if len(len(my_str) != 26):
        return False
# U: Reverse the list compeletely without using slicing
# P: Two pointer technique. Initialize variables at left and right and swap points while iterating with a for loop.
def reverse_list(lst):
    left = 0
    right = len(lst) - 1

    while left < right:
        lst[left], lst[right] = lst[right], lst[left]
        left += 1
        right -= 1
    return lst

# Write a function sort_list_by_parity() that takes in an integer list nums as a parameter and 
# moves all the even integers at the beginning of the list followed by all the odd integers. 
# The function returns any list that satisfies this condition.
# Understand: Update the list so that even integers are in the beginning and odd numbers follow, liek a parity
# Plan: We will do this using the two pointer technique. Initialize a variable left and right, iterate right to search/compare even numbers
# allowing  us to update the left position which is still at beginning and iterate to the next index for the next possible even number.
# Rinse and repeat with your abstracted solution
def sort_array_by_parity(nums):
    left = 0
    right = len(nums) - 1
    while left < right:
        if nums[right] % 2 == 0:
            nums[right], nums[left] = nums[right], nums[left]
            left += 1
        right -= 1
    return nums

nums = [3,1,2,4]
nums2 = [0]
print(sort_array_by_parity(nums))
print(sort_array_by_parity(nums2))


    

        


