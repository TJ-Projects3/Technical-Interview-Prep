# Given two string arrays word1 and word2, return True if the two arrays represent the same string, and False otherwise.
# A string is represented by an array if the array elements concatenated in order forms the string.

# def are_equivalent(word1, word2):
#     return "".join(word1) == "".join(word2)

# word1 = ["bat", "man"]
# word2 = ["b", "atman"]
# print(are_equivalent(word1, word2))

# # Write a function add_matrices() that accepts to n x m matrices matrix1 and matrix2. 
# # The function should return an n x m matrix sum_matrix that is the sum of the given matrices such that each value
# # in sum_matrix is the sum of values of corresponding elements in matrix1 and matrix2.

# # Understand: We will be adding the two matrices and returning a matrix with their totals at each position.
# # matrix1[0][0] + matrix2[0][0]
# # matrix1[0][1] + matrix2[0][1]
# # .....
# # Returns a new matrix
# # Plan: We will use a double for loop to access all possible indices and add them together. It is likely we will have to make a new list
# # as we don't know what limitations the 2 matrices may have, they could be different.

# def add_matrices(matrix1, matrix2):
#     rows, cols = len(matrix1), len(matrix1[0])
#     new_lst = [[0] * cols for i in range(rows)]

#     for i in range(rows):
#         for j in range(cols):
#             new_lst[i][j] = matrix1[i][j] + matrix2[i][j]
#     return new_lst


# matrix1 = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]

# matrix2 = [
#     [9, 8, 7],
#     [6, 5, 4],
#     [3, 2, 1]
# ]

# print(add_matrices(matrix1, matrix2))


# # Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that 
# # i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

# # Notice that the solution set must not contain duplicate triplets.

# # Understand: We are finding 3 unique indices where their elements together add up to zero.
# # Plan: We will use a triple loop to search all possible elements and add the indices to see which equal zero.

def three_sum(nums):
    if not nums or nums == []:
        return []    
    n, res = len(nums), []
    for i in range(0, n, 3):
        for j in range(1, n, 2):
            for k in range(2, n, 1):
                if nums[i] + nums[j] + nums[k] == 0:
                    res.append([nums[i], nums[j], nums[k]])
    return res

nums = [-1, 0, 1, 2, -1, -4]
print(three_sum(nums))

nums = [0, 1, 1]
print(three_sum(nums))

nums = [0, 0, 0]
print(three_sum(nums))

# Write a function linear_search() to help Winnie the Pooh locate his lost items. 
# The function accepts a list items and a target value as parameters. The function should return 
# the first index of target in items, and -1 if target is not in the lst. Do not use any built-in functions.

# Accepts list and target value in parameters
# Target will be a string
# Looking for a specific value in a list

# def linear_search(lst, target):
# 	# Run a for loop to iterate through the list
#         # if i == target:
#         # return target
#     # If target is not in the lsit (outside of the loop) return -1
#     for i in range(len(lst)):
#         if lst[i] == target:
#             return i
#     return -1

# items = ['haycorn', 'haycorn', 'haycorn', 'hunny', 'haycorn']
# target = 'hunny'
# print(linear_search(items, target))

# items = ['bed', 'blue jacket', 'red shirt', 'hunny']
# target = 'red balloon'
# print(linear_search(items, target))


# Tigger has developed a new programming language Tiger with only four operations and one variable tigger.
# bouncy and flouncy both increment the value of the variable tigger by 1.
# trouncy and pouncy both decrement the value of the variable tigger by 1.
# Initially, the value of tigger is 1 because he's the only tigger around! 
# Given a list of strings operations containing a list of operations, 
# return the final value of tigger after performing all the operations.

# value tigger
# list of strings to iterate through
# increment/decrement based off values

# def final_value_after_operations(operations):
# 	tigger = 1
# 	for i in operations:
# 		if i == "bouncy" or i == "flouncy":
# 			tigger += 1
			
# 		if i == "trouncy" or i == "pouncy":
# 			tigger -= 1
# 	return tigger


# operations = ["trouncy", "flouncy", "flouncy"]
# print(final_value_after_operations(operations))

# operations = ["bouncy", "bouncy", "flouncy"]
# print(final_value_after_operations(operations))

# Given two lists of strings artists and set_times of length n, write a function lineup() that maps each artist to their set time.
# An artist artists[i] has set time set_times[i]. Assume i <= 0 < n and len(artists) == len(set_times).
#   V           V
# ["Big Cat", "Snoop"]
# ["9:00PM", "12:00PM"]
# {"Big Cat": "9:00PM", "Snoop": "12:00PM"}
# def lineup(artists, set_times):
#     # Dictionary
# 	result = {}
# 	# For loop
# 	for i in range(len(artists)):
# 	# Since lengths are equal we'll iterate through both with one pointer
# 	# As we loop through assign artists[i] as the key and set_times[i] as the value in the dictionary
# 		result[artists[i]] = set_times[i]
# 	# Return the dictionary
# 	return result

# artists1 = ["Kendrick Lamar", "Chappell Roan", "Mitski", "Rosalia"]
# set_times1 = ["9:30 PM", "5:00 PM", "2:00 PM", "7:30 PM"]

# artists2 = []
# set_times2 = []

# print(lineup(artists1, set_times1))
# print(lineup(artists2, set_times2))

# You are designing an app for your festival to help attendees have the best experience possible! As part of the application, 
# users will be able to easily search their favorite artist and find out the day, time, and stage the artist is playing at. 
# Write a function get_artist_info() that accepts a string artist and a dictionary festival_schedule mapping artist's names to dictionaries 
# containing the day, time, and stage they are playing on. Return the dictionary containing the information about the given artist.
# If the artist searched for does not exist in festival_schedule, return the dictionary {"message": "Artist not found"}.

# We're trying to get the schedule (dictionary inside the dictionary, value of the key) for a given artist name (key, string) inside festival_schedule
# def get_artist_info(artist, festival_schedule):
# # 	# Check if the artist is in the festival schedule
# 	if artist in festival_schedule:
# 		return festival_schedule[artist]
# # 	# If he is then return the value of the artist key
# # 	# else return {"message": "Artist not found"}
# 	else:
# 		return {"message": "Artist not found"}
	
# festival_schedule = {
#     "Blood Orange": {"day": "Friday", "time": "9:00 PM", "stage": "Main Stage"},
#     "Metallica": {"day": "Saturday", "time": "8:00 PM", "stage": "Main Stage"},
#     "Kali Uchis": {"day": "Sunday", "time": "7:00 PM", "stage": "Second Stage"},
#     "Lawrence": {"day": "Friday", "time": "6:00 PM", "stage": "Main Stage"}
# }

# print(get_artist_info("Blood Orange", festival_schedule)) 
# print(get_artist_info("Taylor Swift", festival_schedule))

# A dictionary ticket_sales is used to map ticket type to number of tickets sold. Return the total number of tickets of all types sold.

# Ticket types are mapped to their number of tickets sold in that type. Add together all the values in the hashmap to get the total # of tickets sold.

# def total_sales(ticket_sales):
# 	# Initialize a sum since we're adding a for a total
# 	total = 0
# 	# As we iterate using a for loop, we'll add the values from the hashmap to the sum
# 	for i in ticket_sales:
# 		total += ticket_sales.get(i, 0) # Getting the value from the key i with the get function
# 	# After the loop, return sum
# 	return total

# ticket_sales = {"Friday": 200, "Saturday": 1000, "Sunday": 800, "3-Day Pass": 2500}
# ticket_sales1 = {"Friday": 0, "Saturday": 10000, "Sunday": 833, "3-Day Pass": -2500}

# print(total_sales(ticket_sales))
# print(total_sales(ticket_sales1))

# Captain Blackbeard has a treasure map with several clues that point to different locations on an island. 
# Each clue is associated with a specific location and the number of treasures buried there. Given a dictionary treasure_map 
# where keys are location names and values are integers representing the number of treasures buried at those locations, 
# write a function total_treasures() that returns the total number of treasures buried on the island.

def total_treasures(treasure_map):
    # Initialize sum
    total = 0
    # Use a for loop to iterate through treasure_map
    for i in treasure_map:
        # Add the values in the dictionary to the total using get function syntax
        total += treasure_map.get(i, 0)
    # AFTER the loop, return sum.
    return total

treasure_map1 = {
    "Cove": 3,
    "Beach": 7,
    "Forest": 5
}

treasure_map2 = {
    "Shipwreck": 10,
    "Cave": 20,
    "Lagoon": 15,
    "Island Peak": 5
}

# print(total_treasures(treasure_map1)) 
# print(total_treasures(treasure_map2))

# Taken captive, Captain Anne Bonny has been smuggled a secret message from her crew. She will know she can trust the message if it 
# contains all of the letters in the alphabet. Given a string message containing only lowercase English letters and whitespace, write a 
# function can_trust_message() that returns True if the message contains every letter of the English alphabet at least once, and False otherwise.

def can_trust_message(message):
    # Edge case: if len(message) < 26: automatically false
    # Initialize a set called seen
    # for i in message, if i not in seen: seen.add(...)
    # if len(seen) <= 26: return True
    
    if len(message) < 26:
        return False
    
    seen = set()
    
    for i in message:
        if i != " ":
            seen.add(i)
            
    return len(seen) == 26

# message1 = "sphinx of black quartz judge my vow"
# message2 = "trust me"

# print(can_trust_message(message1))
# print(can_trust_message(message2))

# Write a function print_todo_list() that accepts a list of strings named tasks. The function should then number 
# and print each task on a new line using the format:

# Pooh's To Dos:
# 1. Task 1
# 2. Task 2
# ...

def print_todo_list(task):
    if not task:
        print("Pooh's To Dos:")
        return
    
    # Have a result with Pooh's To Dos: and a newline at then end
    result = "Pooh's To Dos:\n"
    for i in range(len(task)):
        # As you go through tasks, increment each one with its number bullet (front) and a newline (end).
        result += f"{i + 1}. {task[i]}\n"
    print(result.rstrip())
    return

# task = ["Count all the bees in the hive", "Chase all the clouds from the sky", "Think", "Stoutness Exercises"]
# print_todo_list(task)

# task = []
# print_todo_list(task)

# Signs in the Hundred Acre Wood have been losing letters as Tigger bounces around 
# stealing any letters he needs to spell out his name. Write a function tiggerfy() that accepts 
# a string s, and returns a new string with the letters t, i, g, e, and r removed from it.

def tiggerfy(s):
    # We want to remove any occurences of t, i, g, e, or r from the string in-place and return the new
    # string
    # Build the string by iterating it into the result string if it is not t, i, g, e, or r
    result = ""
    letter_check = ["t", "i", "g", "e", "r"] # Still O(1) because its a set length of the constant 5
    for i in s:
        if i.lower() not in letter_check:
            result += i
    return result
        
# s = "suspicerous"
# tiggerfy(s)

# s = "Trigger"
# tiggerfy(s)

# s = "Hunny"
# tiggerfy(s)


def tiggerfy_two(word):
    # T-I-Double Guh-Er: That spells Tigger! Write a function tiggerfy() that accepts a 
    # string word and returns a new string that removes any substrings t, i, gg, and er from word. 
    # The function should be case insensitive.
    # Convert the word to lowercase using lower function for case insensitivity
    lowercase_word = word.lower()
    # Iteratively replace all the substrings given in the problem with nothing
    lowercase_word = lowercase_word.replace("t", "")
    lowercase_word = lowercase_word.replace("i", "")
    lowercase_word = lowercase_word.replace("gg", "")
    lowercase_word = lowercase_word.replace("er", "")

    # After covering all leters/substrings, return the modified word
    return lowercase_word

# word = "Trigger"
# print(tiggerfy_two(word))

# word = "eggplant"
# print(tiggerfy_two(word))

# word = "Choir"
# print(tiggerfy_two(word))

# Example Output:

# "r"
# "eplan"
# "Chor"

# Given an array nums with n integers, write a function non_decreasing() that checks if nums could become
#  non-decreasing by modifying at most one element.
# We define an array is non-decreasing if nums[i] <= nums[i + 1] holds for every i (0-based) such that (0 <= i <= n - 2).

def non_decreasing(nums):
	# We will use a for loop in this problem to touch every nums value and compare it
    # We will keep a count of values that are greater than the next element and if the count exceeds 1, we return False
    count, i = 0, 0
    while i + 1 < len(nums):
        if nums[i] > nums[i + 1]:
            count += 1

            if count > 1:
                return False
        # If we have more than one error, we already know this cannot be fixed
        
            if i == 0 or nums[i - 1] <= nums[i + 1]:
                nums[i] = nums[i + 1]
            else:
                nums[i + 1] = nums[i]
        i += 1
    return True
    # We aren't just counting the amount of errors
    # We are to see if we can actually fix that one modification

# Example Usage:

nums = [4, 2, 2, 0]
print(non_decreasing(nums))

nums = [4, 2, 1]
print(non_decreasing(nums))
        

