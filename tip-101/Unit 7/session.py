"""
Given an integer n, return True if n is a power of four. Otherwise, return False.
An integer n is a power of four if there exists an integer x such that n == 4ˣ.
Solve the problem recursively. What is the time complexity of this function? What is the space complexity?
"""
def is_power_of_four(n):
	if n == 1:
		return True
	if n == 0 or n < 0:
		return False
        
	if n % 4 != 0:
		return False
	else:
		return is_power_of_four(n//4)
	
# print(is_power_of_four(25))
# print(is_power_of_four(16))
# print(is_power_of_four(64))
# print(is_power_of_four(0))

"""
Binary search is a searching algorithm that allows us to efficiently find the index of a given value within a sorted list. 
Given the recursive solution for binary search below, implement an iterative (non-recursive) implementation of binary search.
Evaluate the time and space complexity of your implementation.
"""
def binary_search_recursive(arr, target, left, right):
    if left > right:
        return -1  # Base case: target not found within bounds

		# find middle index of list
    mid = (left + right) // 2
    
    # If the middle element is the target, return its index
    if arr[mid] == target:
        return mid
    # If the target is less than the middle element, search the left half
    elif arr[mid] > target:
        return binary_search_recursive(arr, target, left, mid - 1)
    # If the target is greater than the middle element, search the right half
    else:
        return binary_search_recursive(arr, target, mid + 1, right)

def binary_search_iterative(arr, target):
      left, right = 0, len(arr) - 1

      while left <= right:
            mid = (left + right)//2

            if arr[mid] == target:
                  return mid
            
            if arr[mid] < target:
                  left = mid + 1
            else:
                  right = mid - 1
      return -1


"""
Given a sorted list of integers and a value x, return the index of the ceiling of x.
The ceiling of x is the smallest element in the array larger than or equal to x.
If there is no ceiling of x, return -1.
Evaluate the time and space complexity of your function.
"""
# U: This problem is asking us to find the ceiling of x. The ceiling of x is the smallest value in the list that is greater
# than x. If there is no ceiling, return -1.
# P: We will use iterative binary search and leverage the middle index to continuously cut the list in half
def find_ceiling(lst, x):
    left, right = 0, len(lst) - 1

    while left <= right:
      mid = (left + right)// 2
      
      if lst[mid] == x:
            return mid

      if lst[mid] > x:
            right = mid - 1
      else:
            left = mid + 1
      
    if left < len(lst) and lst[left] >= x:
      return left
    return -1

"""
Ternary search is a search algorithm that, similar to binary search, works on a sorted array. 
However, instead of dividing the search interval into two halves (as in binary search), ternary search divides it into three parts,
using two midpoints. This reduces the problem size to approximately one-third in each step, rather than one-half.
Given the pseudocode for ternary_search() below, implement the function. Evaluate the time and space complexity of your solution
"""
def ternary_search(lst, target):
  # Divide the array into three parts using two mid points (mid1 and mid2).
  left, right = 0, len(lst) - 1

  while left <= right:
      mid1 = right - (right - left) // 3
      mid2 = left + (right - left) // 3

      if lst[mid1] == target:
            return mid1

      if lst[mid2] == target:
            return mid2

      if lst[mid1] > target:
            right = mid1 - 1

      if lst[mid1] < target and lst[mid2] > target:
            left = mid1 + 1
            right = mid2 - 1
      
      if lst[mid2] < target:
            left = mid2 + 1
  return -1
  # While the lower bound is less than or equal to the upper bound:
	  # Compare the target value with the values at mid1 and mid2:
	      # If the target value matches mid1 or mid2
		      # the search is successful.
	      # If the target is less than the value at mid1
		      # search between the lower bound and mid1 - 1.
	      # If the target is between mid1 and mid2
		      # search between mid1 + 1 and mid2 - 1.
	      # If the target is greater than the value at mid2
		      # search between mid2 + 1 and the upper bound.
  # Return -1, indicating the target is not in the array.

lst1 = [2, 4, 6, 8, 10, 12, 14] 
# print(ternary_search(lst1, 7))        

"""
Given a string, return True if it is a nesting of zero or more pairs of parentheses. 
Return False otherwise. A valid pair of parentheses is defined as (). 
The input string will only contain the characters ( or ). Your solution must be recursive.
Evaluate the time and space complexity of your solution.
"""

def is_nested(paren_s):

      if len(paren_s) % 2 != 0:
            return False
      
      if len(paren_s) == 0:
           return True
      
      if paren_s[0] == "(" and paren_s[-1] == ")":
            return is_nested(paren_s[1:-1])
      
      return False

input = "()"
# print(is_nested(input))

"""
Given the base case and recursive case, write a recursive function string_length() that returns the length of a string s 
without using the built-in len() function. Base Case: An empty string should have size 0.
Recursive Case: We can restate the problem to say that the string length is 1 + the length of s[1:]

UNDERSTAND: This is a recursive problem where the question is asking us to find the length of a string
without the len() function shortcut. We must implement a base case where an empty string has the size 0,
and a recursive case where it keeps we cut down the size of the string by one while calling the function again with that
string and adding by 1. We do this all in a return statement for the recursive case.

PLAN: We will implemwnt a recursive solution with the base case of an empty string returning size 0. Then we will
use a recursive case of 1 + len(s[1:]) to keep adding 1 when the string is valid.
"""

def string_length(s):
     if s == "":
          return 0
     else:
          return 1 + string_length(s[1:])

wordOne = "ajfhe"
wordTwo = "hireme"
wordThree = "love"
wordFour = "lolololololol"
# print(string_length(wordOne))
# print(string_length(wordTwo))
# print(string_length(wordThree))
# print(string_length(wordFour))

"""
Given a non-negative integer n, write a function sum_digits() that calculates and returns the sum of its digits recursively.

Evaluate the time and space complexity of your solution.

UNDERSTAND: Given an input n, we can write a function that calculates and then returns the sum of its digits recurisvely.

IMPLEMENT: We will implement this by using a recursive solution, taking in a base case, and that base case will be if s == "",
indicating an empty string, else, we keep shortening the string by taking out a digit and adding it to the recursive call.
"""
def sum_digits(n):
     # If the number is a single digit
     if n % 10 == n:
          return n
     else:
          return n % 10 + sum_digits(n // 10) # // gives us integer only 523// 10 = 52, instead of 52.3. Removes back digits.

# print(sum_digits(523))
# print(sum_digits(10))
# print(sum_digits(1))


"""
Given a sorted list of integers containing only 0s and 1s, 
count the total number of 1s in the array in O(log n) time.

INPUTS: An array of integers of 1s and 0s
OUTPUTS: total count of ones in the array
Cases/Considerations: lst must not be 0, lst has to have 1s in it unless return 0 for both of these
Another consideration is that the list is SORTED
Examples:
[0,0,0,1,1,1]
Output = 3

[0,1]
Output = 1

[0,0,0]
Output = 0

PLAN: We shall find the first occurence of 1 with binary search, then because of the list being sorted, 
we can assume the rest of the list after the first occurence of 1  are ones themselves. So we keep shortening our problem
until our case is reached and we find the first occurence of 1, then we take count the rest of the list moving forward.
"""
def count_ones(lst):
     left, right = 0, len(lst) - 1
     count = 0

     if 1 not in lst:
          return 0

     while left <= right:
        mid = (left + right) // 2
        # SORTED LIST
        if lst[mid] == 1:
            if mid == 0 or lst[mid - 1] == 0:
                 return len(lst) - mid
            else:
                 right = mid - 1
        else:
             left = mid + 1
     return 0
     
# amounts = [0, 0, 0, 0, 1, 1, 1]
# print(count_ones(amounts))


def factorial(n):
     if n == 0: # Base Case
          return 1
     
     return n * factorial(n-1) # Recursive Case

print(factorial(6))
     
               
                