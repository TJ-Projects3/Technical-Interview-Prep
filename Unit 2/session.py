# Write a function is_subsequence() that takes in a list of integers lst and a list of integers sequence as parameters.
#  Given these two lists, determine whether the sequence list is a subsequence of the lst list. 
# A subsequence of a list is a set of numbers that aren't necessarily adjacent but are in the same relative order as they appear in the list. 
# Return True if sequence is a subsequence, and False otherwise.
def is_subsequence(lst, sequence):
    for i in sequence:
        if i not in lst:
            return False
    return True
        

lst = [6, 1, 4, -10, -1, 5]
sequence = [1, 6, -1, 10]
# print(is_subsequence(lst, sequence))

# Write a function create_dictionary() that takes in a list of keys and a list of values as parameters.
#  The function returns a dictionary where each item in keys is paired with a corresponding item in values.
# keys[i] should be paired with values[i] in the dictionary where 0 <= i <= len(keys). 
# You may assume keys and values are the same length.

# Understand: We are going to use a dictionary. Basically, the problem is asking us to take 2 lists as information to make a dictionary
# with each item by pairing them by index
# Plan: Initializing a dict then initializing a for loop, in which we will access these variables as we iterate through the for loop 
# and assign them to a dictionary

def create_dictionary(keys, values):
    dict = {}
    for i in range(len(keys)):
        dict[keys[i]] = values[i]
    return dict

keys = ["peanut", "dragon", "star", "pop", "space"]
values = ["butter", "fly", "fish", "corn", "ship"]
print(create_dictionary(keys, values))

# Write a function print_pair() that takes in a dictionary dictionary and a key target as parameters. 
# The function looks for the target and when found, it prints the key and it's associated value as
#  "Key: <key>" followed by "Value: <value>".
#  If target is not in dictionary, print "That pair does not exist!".
# Understand: We know that we are searching a particular dictionary for a key, and printing that key and its value if we find it.
# If we dont find it we have a base case "The pair doesn't exist!"
# Plan: We will use an if in condition (naturally iterates) to check if the target is in th dict, and print key and value if it is
# and print th base case if it isn't  
def print_pair(dictionary, target):
    if target in dictionary:
        print("Key: " + target)
        print("Value: " + dictionary[target])
    else:
        print("That pair does not exist!")

dictionary = {"spongebob": "squarepants", "patrick": "star", "squidward": "tentacles"}
# print_pair(dictionary, "patrick")
# print_pair(dictionary, "plankton")
# print_pair(dictionary, "spongebob")

# Write a function index_to_value_map() that takes in a list lst and returns a dictionary that maps the index of each element in lst to its value.
# Understand: Wants to take index of each element in a list and their value to make a dictionary.
# Plan: We will initialize a dict and for loop to access each index and create items in the dictionary.
def index_to_value_map(lst):
    dict = {}
    for i in range(len(lst)):
        dict[i] = lst[i]
    return dict

listOne = ["apple", "banana", "cherry"]

# print(index_to_value_map(listOne))

def count_mississippi(limit):
    for num in range(1, limit):
        print( f"{num} mississippi")

count_mississippi(5)

