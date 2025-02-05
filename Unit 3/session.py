# # Write a function swap_ends() that accepts a string my_str as a parameter and 
# # returns a new string where the first and last characters from my_str are swapped.
# def swap_ends(my_str):
#     str = ""
#     for i in range(len(my_str)):
#         if (i == 0):
#             str += my_str[len(my_str) - 1]
#         elif(i == len(my_str) - 1):
#             str += my_str[0]
#         else:
#             str += my_str[i]
#     return str

# stringOne = "gonow"
# print(swap_ends(stringOne))

# # Write a function is_pangram() that takes in a string my_str as a parameter
# #  and returns True if the string is a pangram and False if not.
# #  A pangram is a sentence containing every letter in the English alphabet.
# def is_pangram(my_str):
#     if len(len(my_str) != 26):
#         return False
# # U: Reverse the list compeletely without using slicing
# # P: Two pointer technique. Initialize variables at left and right and swap points while iterating with a for loop.
# def reverse_list(lst):
#     left = 0
#     right = len(lst) - 1

#     while left < right:
#         lst[left], lst[right] = lst[right], lst[left]
#         left += 1
#         right -= 1
#     return lst

# # Write a function sort_list_by_parity() that takes in an integer list nums as a parameter and 
# # moves all the even integers at the beginning of the list followed by all the odd integers. 
# # The function returns any list that satisfies this condition.
# # Understand: Update the list so that even integers are in the beginning and odd numbers follow, liek a parity
# # Plan: We will do this using the two pointer technique. Initialize a variable left and right, iterate right to search/compare even numbers
# # allowing  us to update the left position which is still at beginning and iterate to the next index for the next possible even number.
# # Rinse and repeat with your abstracted solution
# def sort_array_by_parity(nums):
#     left = 0
#     right = len(nums) - 1
#     while left < right:
#         if nums[right] % 2 == 0:
#             nums[right], nums[left] = nums[right], nums[left]
#             left += 1
#         right -= 1
#     return nums

# nums = [3,1,2,4]
# nums2 = [0]
# print(sort_array_by_parity(nums))
# print(sort_array_by_parity(nums2))

# Write a function vowel_count() that takes in a string s as a parameter and returns the number of vowels in the given string.

def vowel_count(s):
    vowels = ["a", "e", "i", "o", "u"]
    count = 0

    for char in s:
        if char in vowels:
            count += 1
    return count


# Write a function remove_char() that takes in a string s and an integer n as parameters, 
# The function returns a new string with the nth character removed where 0 < n < len(s).

def remove_char(s, n):
    return s[0:n] + s[n+1:len(s)]

# Write a function reverse_sentence() that takes in a string sentence as a parameter and returns the string with the sentence 
# but with the order of the words reversed. The sentence will only contain alphabetic characters and spaces to separate the words. 
# If there is only one word in the sentence, the function returns the original string.
# Understand: We are asked to reverse the words of the sentence, not the letters. If the string only has one word, we'll simply return that word
# Plan: We will create a new string and use a backwards for loop to iterate the words into that new string backwards.
def reverse_sentence(sentence):
    sentence_list = sentence.split()
    if len(sentence_list) <= 1:
        return sentence
    left, right = 0, len(sentence_list) - 1
    while left < right:
        sentence_list[left], sentence_list[right] = sentence_list[right], sentence_list[left]
        left += 1
        right -= 1
    return " ".join(sentence_list)

# Write a function that takes in a string my_str as a parameter and performs basic string compression using counts of repeated characters.
# For example, the string "aabcccccaaa" would become "a2b1c5a3". If the compressed string does not become smaller than the original string, 
# return the original string. Assume the string only has alphabetic characters.
# Understand: We are given a string that we have to compress using the counts of repeated letters next to their single letter that was repeated
# in sequences.
# Plan: We will use a for loop focusing on counting the current letter until we see a new letter. When we see a new one, we will add the past letter 
# and the count compress in our result string, then start a new count with the new current letter as our focus, and so on, repeating the steps.

def compress_string(my_str):
    current_ltr, count = my_str[0], 1
    res = ""
    for char in range(1,len(my_str)):
        if my_str[char] == current_ltr:
            count += 1
        else:
            res += (current_ltr + str(count))
            count = 1
            current_ltr = my_str[char]
    res += (current_ltr + str(count))
    return res if len(res) < len(my_str) else my_str
testCase = "abbcddddd"
print(compress_string(testCase))

# Write a function partition_labels() that takes in a string s as a parameter. 
# s consists of lowercase letters and represents the order of characters as they appear in a document. 
# The function partitions s into as many parts as possible so that each unique letter appears in at most one part, 
# and returns a list of integers representing the size of these parts.

# Understand: We are splitting the list so that each unique letter occurences will appear in one part and return a list of integers
# with the size of these parts.

def partition_label(s):
    pass




    

        


