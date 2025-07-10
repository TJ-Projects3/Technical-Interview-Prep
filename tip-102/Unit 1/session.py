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

# def three_sum(nums):
#     if not nums or nums == []:
#         return []    
#     n, res = len(nums), []
#     for i in range(0, n, 3):
#         for j in range(1, n, 2):
#             for k in range(2, n, 1):
#                 if nums[i] + nums[j] + nums[k] == 0:
#                     res.append([nums[i], nums[j], nums[k]])
#     return res

# nums = [-1, 0, 1, 2, -1, -4]
# print(three_sum(nums))

# nums = [0, 1, 1]
# print(three_sum(nums))

# nums = [0, 0, 0]
# print(three_sum(nums))

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
def get_artist_info(artist, festival_schedule):
# 	# Check if the artist is in the festival schedule
	if artist in festival_schedule:
		return festival_schedule[artist]
# 	# If he is then return the value of the artist key
# 	# else return {"message": "Artist not found"}
	else:
		return {"message": "Artist not found"}
	
festival_schedule = {
    "Blood Orange": {"day": "Friday", "time": "9:00 PM", "stage": "Main Stage"},
    "Metallica": {"day": "Saturday", "time": "8:00 PM", "stage": "Main Stage"},
    "Kali Uchis": {"day": "Sunday", "time": "7:00 PM", "stage": "Second Stage"},
    "Lawrence": {"day": "Friday", "time": "6:00 PM", "stage": "Main Stage"}
}

print(get_artist_info("Blood Orange", festival_schedule)) 
print(get_artist_info("Taylor Swift", festival_schedule))

# A dictionary ticket_sales is used to map ticket type to number of tickets sold. Return the total number of tickets of all types sold.

# Ticket types are mapped to their number of tickets sold in that type. Add together all the values in the hashmap to get the total # of tickets sold.

def total_sales(ticket_sales):
	# Initialize a sum since we're adding a for a total
	total = 0
	# As we iterate using a for loop, we'll add the values from the hashmap to the sum
	for i in ticket_sales:
		total += ticket_sales.get(i, 0) # Getting the value from the key i with the get function
	# After the loop, return sum
	return total

ticket_sales = {"Friday": 200, "Saturday": 1000, "Sunday": 800, "3-Day Pass": 2500}
ticket_sales1 = {"Friday": 0, "Saturday": 10000, "Sunday": 833, "3-Day Pass": -2500}

print(total_sales(ticket_sales))
print(total_sales(ticket_sales1))
	
    

			