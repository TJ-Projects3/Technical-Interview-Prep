# Write a function is_subsequence() that takes in a list of integers lst and a list of integers sequence as parameters.
#  Given these two lists, determine whether the sequence list is a subsequence of the lst list. 
# A subsequence of a list is a set of numbers that aren't necessarily adjacent but are in the same relative order as they appear in the list. 
# Return True if sequence is a subsequence, and False otherwise.
# We are trying to find out if sequence is a subsequence of list, meaning the numbers are in there in appearing in order, but not next to each other.
# We will use the two pointer method to have pointers, one in lst, and one in subsequence.

def is_subsequence(lst, sequence):
    left, right = 0, 0

    if not sequence:
        return True

    if not lst:
        return False

    while left < len(sequence) and right < len(lst):
        if sequence[left] == lst[right]:
            left, right = left + 1, right + 1
        else:
            right += 1
    return left == len(sequence)




lst_one = [5, 1, 22, 25, 6, -1, 8, 10]
lst_two = [1, 2, 3]
sequence = [1, 6, -1, 10]
sequenceTwo = [2, 9, -2, 11]
sequenceThree = [3, 2, 1]
print(is_subsequence(lst_two, sequenceThree))

# # Write a function create_dictionary() that takes in a list of keys and a list of values as parameters.
# #  The function returns a dictionary where each item in keys is paired with a corresponding item in values.
# # keys[i] should be paired with values[i] in the dictionary where 0 <= i <= len(keys). 
# # You may assume keys and values are the same length.

# # Understand: We are going to use a dictionary. Basically, the problem is asking us to take 2 lists as information to make a dictionary
# # with each item by pairing them by index
# # Plan: Initializing a dict then initializing a for loop, in which we will access these variables as we iterate through the for loop 
# # and assign them to a dictionary

# def create_dictionary(keys, values):
#     dict = {}
#     for i in range(len(keys)):
#         dict[keys[i]] = values[i]
#     return dict

# keys = ["peanut", "dragon", "star", "pop", "space"]
# values = ["butter", "fly", "fish", "corn", "ship"]
# print(create_dictionary(keys, values))

# # Write a function print_pair() that takes in a dictionary dictionary and a key target as parameters. 
# # The function looks for the target and when found, it prints the key and it's associated value as
# #  "Key: <key>" followed by "Value: <value>".
# #  If target is not in dictionary, print "That pair does not exist!".
# # Understand: We know that we are searching a particular dictionary for a key, and printing that key and its value if we find it.
# # If we dont find it we have a base case "The pair doesn't exist!"
# # Plan: We will use an if in condition (naturally iterates) to check if the target is in th dict, and print key and value if it is
# # and print th base case if it isn't  
# def print_pair(dictionary, target):
#     if target in dictionary:
#         print("Key: " + target)
#         print("Value: " + dictionary[target])
#     else:
#         print("That pair does not exist!")

# dictionary = {"spongebob": "squarepants", "patrick": "star", "squidward": "tentacles"}

# # print_pair(dictionary, "patrick")
# # print_pair(dictionary, "plankton")
# # print_pair(dictionary, "spongebob")

# # Write a function index_to_value_map() that takes in a list lst and returns a dictionary that maps the index of each element in lst to its value.
# # Understand: Wants to take index of each element in a list and their value to make a dictionary.
# # Plan: We will initialize a dict and for loop to access each index and create items in the dictionary.
# def index_to_value_map(lst):
#     dict = {}
#     for i in range(len(lst)):
#         dict[i] = lst[i]
#     return dict

# listOne = ["apple", "banana", "cherry"]

# # print(index_to_value_map(listOne))

# def count_mississippi(limit):
#     for num in range(1, limit):
#         print( f"{num} mississippi")

# count_mississippi(5)

# # Write a function dict_difference() that takes two dictionaries and returns a new dictionary that 
# # contains only the key-value pairs found exclusively in the first dictionary but not in the second.

# # def dict_difference(d1, d2):
# #     return {k: d1[k] for k in d1 if k not in d2 or d1[k] != d2[k]}

# # res = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
# # res1 = {'b': 2, 'd': 1}

# # print(dict_difference(res, res1))


# # Write a function pop_stock() that takes a dictionary of items items that keeps track of an item and its stock quantity, 
# # an item_name, and a quantity to be removed as parameters. The function should remove the specified quantity for that item.
# # If the item does not exist, return the string "Item does not exist." 
# # If the specified quantity is greater than the stock, return a string "Not enough stock."
# # If the specified item and quantity do exist within items, decrement the item's stock by the specified quantity and return the updated dictionary.

# # Understand: We are storing items with their name and price to a dictionary, we will handle edge cases if the item name isnt in the list, the quantity
# # asked for isnt enough, and more. If all things sufficient, we will decrement the count of the item in the dictionary by the requested quantity.
# # Plan: The dictionary is given, we will use if in and not in to handle edge cases and if everything is present, subtract by the quantity for our function.
# def pop_stock(items, item_name, quantity):
#     if item_name not in items:
#         return "Item does not exist"
#     else:
#         if quantity > items[item_name]:
#             return "Not enough stock"
#         else:
#             items[item_name] -= quantity
#             return items

# items = {"chocolate": 20, "candy": 5, "chips": 10}

# resultA = pop_stock(items, "candy", 2)
# print(resultA)
# resultB = pop_stock(items, "candy", 5)
# print(resultB)
# resultC = pop_stock(items, "lollipops", 5)
# print(resultC)
# resultD = pop_stock(items, "chocolate", 5)
# print(resultD)


# # {"chocolate": 20, "candy": 3, "chips": 10}
# # Not enough stock
# # Item does not exist
# # {"chocolate": 15, "candy": 3, "chips": 10}

# # Write a function average_book_ratings(), that calculates the average rating for each book in a collection. 
# # The function takes one parameter: a dictionary book_ratings where each key-value pair represents a book title and a list of its ratings, respectively. 
# # Ratings are represented as floating-point numbers. The function should return a new dictionary with book titles as keys and their average rating.

# # Understand: We are creating a new dictionary from an existing dictionary, using the key (book name), and value (list of ratings) from the original to create
# # a dictionary that has the book name key and instead of a list, it has the average rating from that list. Return the new dictionary
# # Plan: Create a for loop that loops through dict.items() so that we can iterate through key and value. For the new dictionary while in the for loop,
# # Assign book name to the key and calculate average by dividing total of the list by the length.

# def average_book_ratings(book_ratings):
#     res = {}
#     for k, v in dict.items(book_ratings):
#         average = sum(v)/len(v) # v - list value
#         res[k] = round(average, 1) # k - book name, the key must stay
#     return res # After the loop, return new dictionary


# book_ratings_one = {
#     "The Great Gatsby": [4.5, 3.0, 5.0],
#     "To Kill a Mockingbird": [4.8, 5.0, 4.0, 4.9]
# }

# print(average_book_ratings(book_ratings_one))

# # Write a function restock_inventory() that updates an inventory dictionary based on a restock list. It accepts two parameters:
# # current_inventory: a dictionary where each key-value pair represents an item and its current stock in the inventory 
# # restock_list: a dictionary where each key-value pair represents an item and the quantity to be added to the inventory. 
# # If an item in restock_list is not present in the current_inventory, it should be added. The function should return the 
# # updated dictionary current_inventory.

# # Understand: We are updating the current_inventory with the restock_list, adding to the values of existing keys and adding keys from the restock_list
# # if they aren't already in the current_inventory
# # Plan: Create for loop using dict.items(restock_list), if k not in current_inventory add it, else add the value of that key
# # to the mapping in current stock.

# def restock_inventory(current_inventory, restock_list):
#     # Not creating anything new. Reading and updating to solve problem
#     for k, v in restock_list.items():
#         if k not in current_inventory:
#             current_inventory[k] = v
#         else:
#             current_inventory[k] += v
#     return current_inventory

# current_inventory1 = {
#     "apples": 30,
#     "bananas": 15,
#     "oranges": 10
# }

# restock_list1 = {
#     "oranges": 20,
#     "apples": 10,
#     "pears": 5
# }

# print(restock_inventory(current_inventory1, restock_list1))


# # Write a function hasDuplicates() that takes in a list of integers nums and a positive number k as parameters. 
# # The function returns True if the list contains any duplicate elements within the range 0 to k (inclusive). 
# # If k is greater than the list's length, the solution should check for duplicates in the complete list. The function should return False otherwise.

# # Understand: Within the range 0 to parameter k, return True if there are duplicate numbers within that range. Else return false.
# # If k is larger than list, focus on covering the whole length of the list
# # Plan: Use a set. We will iterate through a for loop for range 0 to k, if iterable is in the set already return True. Otherwise if we get through the
# # whole loop, return False because we found no duplicates in that specified range.

# def hasDuplicates(nums, k):
#     seen = set()

#     if k > len(nums):
#         k = len(nums)

#     for i in range(0, k):
#         if nums[i] in seen:
#             return True
#         seen.add(nums[i])
#     return False

# nums = [5, 6, 8, 2, 6, 4, 9]
# check1 = hasDuplicates(nums, 3)
# print(check1)
# check2 = hasDuplicates(nums, 5)
# print(check2)

# # Write a function divideList() that takes in an integer list nums consisting of 2*n integers as parameters.

# #  The function divides nums into n pairs such that:

# # Each element belongs to exactly one pair
# # The elements present in a pair are equal

# # Return True if nums can be divided into n pairs, otherwise return False.

# # Understand: We are given a list to divide into len(list)/2 pairs. If we can create pairs with the list, return True. Else, return False.
# # Plan: Sandwich pair_count integer. Create a counter dictionary (pair_dict) to get all occurences of each number in the list. Afterwards, 
# # create another for loop that iterates through this pair_dict and as we do so, add to the pair count res[i] hard divided by 2  (//)

# def divideList(nums):
#     pair_dict, pair_count = {}, 0
#     cut = len(nums) // 2

#     for i in nums:
#         pair_dict[i] = pair_dict.get(i, 0) + 1
    
#     for i in pair_dict:
#         divide_pairs = pair_dict[i] // 2
#         pair_count += divide_pairs
    
#     return True if pair_count == cut else False

# nums_example = [3,2,3,2,2,2]
# print(divideList(nums_example))


def get_count(lst):
    res = {}
    for i in lst:
        res[i] = res.get(i, 0) + 1
    return res

new_lst = [1,1,1,4,5,7,8,6,7]
print(get_count(new_lst))

# Write a function is_monotonic() that takes in a list nums as a parameter and checks if it is either monotone increasing or monotone decreasing.
# A list is monotone increasing if every element is either greater than or equal to the element before it.
# A list is monotone decreasing if every element is either less than or equal to the element before it.
# The function should return True if the given list is either monotone increasing or decreasing and False otherwise.
# Hint: This is a lists problem

# Understand: We are determining if the list is monotone decreasing or monotone increasing, meaning the EVERY value is either greater than or equal to
# element before it or every element is either less than or equal to the element before it.
# Plan: For each monotone type, use a for loop to iterate through the elements and return True if each element before is monotone format.
def is_monotonic(nums):
    is_increasing = True # Set boolean to track if the list is increasing
    for i in range(1, len(nums)): # For every element in nums list, starting from to 1 to len(nums) to cover all indices
        if nums[i - 1] > nums[i]: # For our increasing loop, if the element is less than the element before
            is_increasing = False # Set increasing boolean to False, because it's definitely not an increasing monotone
            break # Break off the loop early to save time complexity

    is_decreasing = True # Set boolean for decreasing loop to see if it is actually going to be a monotone decreasing list
    for n in range(1, len(nums)): # For every element in nums list, startngi from 1 to len(nums) to account for every number
        if nums[n - 1] < nums[n]: # If the current element is now greater than the element before the current
            is_decreasing = False # Set is_decreasing to False, because there is no way the list is "monotone decreasing" or a decreasing list
            break # Break early to save time

    return is_increasing or is_decreasing # return boolean to see if one is true or both booleans are False

nums1 = [1,2,2,3,10]
print(is_monotonic(nums1))

nums2 = [12,9,8,3,1]
print(is_monotonic(nums2))

nums3 = [1,1,1]
print(is_monotonic(nums3))

nums4 = [1,9,8,3,5]
print(is_monotonic(nums4))
            


	

