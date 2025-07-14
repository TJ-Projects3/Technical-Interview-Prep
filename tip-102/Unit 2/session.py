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

# def total_treasures(treasure_map):
#     # Initialize sum
#     total = 0
#     # Use a for loop to iterate through treasure_map
#     for i in treasure_map:
#         # Add the values in the dictionary to the total using get function syntax
#         total += treasure_map.get(i, 0)
#     # AFTER the loop, return sum.
#     return total

# treasure_map1 = {
#     "Cove": 3,
#     "Beach": 7,
#     "Forest": 5
# }

# treasure_map2 = {
#     "Shipwreck": 10,
#     "Cave": 20,
#     "Lagoon": 15,
#     "Island Peak": 5
# }

# print(total_treasures(treasure_map1)) 
# print(total_treasures(treasure_map2))

# # Taken captive, Captain Anne Bonny has been smuggled a secret message from her crew. She will know she can trust the message if it 
# # contains all of the letters in the alphabet. Given a string message containing only lowercase English letters and whitespace, write a 
# # function can_trust_message() that returns True if the message contains every letter of the English alphabet at least once, and False otherwise.

def can_trust_message(message):
    # Edge case: if len(message) < 26: automatically false
    # Initialize a set called seen
    # for i in message, (if i not in seen not needed)
    # if  i != " " (whitespace): seen.add(i)
    # if len(seen) <= 26: return True
    
    if len(message) < 26:
        return False #Edge case to see if message is even 26 characters
    
    seen = set() # Initialize set
    
    for i in message: # For every character in message
        if i != " ": # If i is not whitespace
            seen.add(i) # Then add i to the seen set, which ultimately only takes in unique values
            
    return len(seen) == 26 # Return True if length of seen has all 26 letters of alphabet else False

# message1 = "sphinx of black quartz judge my vow"
# message2 = "trust me"

# print(can_trust_message(message1))
# print(can_trust_message(message2))

# # Captain Blackbeard has an integer array chests of length n where all the integers in chests are in the range [1, n] and each integer appears 
# # once or twice. Return an array of all the integers that appear twice, representing the treasure chests that have duplicates.

def find_duplicate_chests(chests):
    # Initialize a set and result array
    # For chest in chests
    # if chest in seen:
    # Add chest to the result array
    # seen.add(chest)
    # Outside of for loop, return result
    seen = set()
    result = []
    for chest in chests:
        if chest in seen:
            result.append(chest)
        seen.add(chest)
    return result

# chests1 = [4, 3, 2, 7, 8, 2, 3, 1]
# chests2 = [1, 1, 2]
# chests3 = [1]

# print(find_duplicate_chests(chests1))
# print(find_duplicate_chests(chests2))
# print(find_duplicate_chests(chests3))


# # Captain Feathersword has found another pirate's buried treasure, but they suspect it's booby-trapped. 
# # The treasure chest has a secret code written in pirate language, and Captain Feathersword believes the trap 
# # can be disarmed if the code can be balanced. A balanced code is one where the frequency of every letter present in the code is equal. 
# # To disable the trap, Captain Feathersword must remove exactly one letter from the message. 
# # Help Captain Feathersword determine if it's possible to remove one letter to balance the pirate code.
# # Given a 0-indexed string code consisting of only lowercase English letters, write a function is_balanced() that 
# # returns True if it's possible to remove one letter so that the frequency of all remaining letters is equal, and False otherwise.

# # "hahahaa"
# # True

def is_balanced(code): # Think like a human in real life for the problem
# # Count the letters
# # Have a copy
# # Remove every letter once using a for loop to see which balances the string
# # If you go through each letter, and nothing balances, return False
    counter = {}
    for i in code:
        counter[i] = counter.get(i,0) + 1
    
    for i in counter:
        counter_copy = counter.copy()
        counter_copy[i] -= 1

        if counter_copy[i] == 0:
            del counter_copy[i]

        values = list(counter_copy.values())

        if len(set(values)) == 1:
            return True
    return False

code1 = "ararrgghh"
code2 = "ha"

# print(is_balanced(code1)) 
# print(is_balanced(code2))

#     # returning True or False based off if we can balance the count by removing one letter
#     # After counting, search for the greatest count and subtract it - 1



# # Captain Feathersword and their crew has discovered a list of gold amounts at various hidden locations on an island. 
# # Each number on the map corresponds to the amount of gold at a specific location. Captain Feathersword already has plenty of loot, 
# # and their ship is nearly full. They want to find two distinct locations on the map such that the sum of the gold amounts at these 
# # two locations is exactly equal to the amount of space left on their ship.

# # Given an array of integers gold_amounts representing the amount of gold at each location and an integer target, 
# # return the indices of the two locations whose gold amounts add up to the target.

# # Assume that each input has exactly one solution, and you may not use the same location twice. You can return the answer in any order.

# # This is a Two Sum solution
# # We want to iterate through a for loop with an enumerate, and subtract the target - value of iterator to see if it exists in the list
# # We can find out if it exists not using a list, but using the direct lookup of a hashmap, which is O(1) by the way
# # We will subtract target - val each loop
# # Remember, we want the indices...

def find_treasure_indices(gold_amounts, target):
#     # Hashmap
#     # For loop
#     # if target - val in the hashmap:
#         # return [something, something] that add up to target
#     # Regardless, keep assigning iterator value to its index.
    res = {}
    for i, val in enumerate(gold_amounts):
        if target - val in res: # 9 - 2 = 7 F # 9 - 7 = 2 T
            return [res[target - val], i] # i = 1, returns [1, 0]
        res[val] = i # {2: 0}

# gold_amounts1 = [2, 7, 11, 15]
# target1 = 9

# gold_amounts2 = [3, 2, 4]
# target2 = 6

# gold_amounts3 = [3, 3]
# target3 = 6

# print(find_treasure_indices(gold_amounts1, target1))  
# print(find_treasure_indices(gold_amounts2, target2))  
# print(find_treasure_indices(gold_amounts3, target3))


# Problem 6: Organize the Pirate Crew
# Captain Blackbeard needs to organize his pirate crew into different groups for a treasure hunt. Each pirate has a unique ID from 0 to n - 1.
# You are given an integer array group_sizes, where group_sizes[i] is the size of the group that pirate i should be in.
# For example, if group_sizes[1] = 3, then pirate 1 must be in a group of size 3.
# Return a list of groups such that each pirate i is in a group of size group_sizes[i].
# Each pirate should appear in exactly one group, and every pirate must be in a group. 
# If there are multiple answers, return any of them. It is guaranteed that there will be at least one valid solution for the given input.

# Based on the value, we will organize the indices into groups of those sizes.
# Count the number of group sizes in hashmap

def organize_pirate_crew(group_sizes):
    group_tracker = {} # Initialize hashmap to track list of each group
    for i in group_sizes: # For every group size in the given list
        group_tracker[i] = [] # Mapping group size to list of pirates
    result = []
    for i, val in enumerate(group_sizes):
        group_tracker[val].append(i) # Append the pirate ID from group_sizes into tracker list

        if len(group_tracker[val]) == val: # If the tracker list is full for a group size
            result.append(group_tracker[val]) # Append the current full group to the result list
            group_tracker[val] = [] # Empty the list for space since one group has been organized and moved to result.
    return result # Return the final result of organized, complete group lists

# group_sizes1 = [3, 3, 3, 3, 3, 1, 3]
# group_sizes2 = [2, 1, 3, 3, 3, 2]
# group_sizes3 = [2, 2]
# group_sizes4 = [2, 2, 1, 1, 1, 3, 3, 3]

# print(organize_pirate_crew(group_sizes1))
# print(organize_pirate_crew(group_sizes2))
# print(organize_pirate_crew(group_sizes3))
# print(organize_pirate_crew(group_sizes4))

# Captain Blackbeard has two treasure maps represented by two strings of the same length map1 and map2. In one step, 
# you can choose any character of map2 and replace it with another character.
# Return the minimum number of steps to make map2 an anagram of map1.
# An Anagram of a string is a string that contains the same characters with a different (or the same) ordering.

def min_steps_to_match_maps(map1, map2):
    if len(map1) != len(map2):
        return None

    counter1 = {}
    counter2 = {}
    diff_count = 0
    
    for i, n in zip(map1, map2):
        counter1[i] = counter1.get(i, 0) + 1
        counter2[n] = counter2.get(n, 0) + 1

    if counter1 == counter2:
        return 0

    for i in counter2:  # For every character in map2
        if i in counter1: # If it's in map1
            diff_count += max(0, counter2[i] - counter1[i]) # Calculate the difference between character count if any
        else:
            diff_count += counter2[i]  # Add count for characters missing in counter1

    return diff_count # Return total mismatching characters in "minimum steps"

map1_1 = "bab"
map2_1 = "aba"
map1_2 = "treasure"
map2_2 = "huntgold"
map1_3 = "anagram"
map2_3 = "mangaar"
map1_4 = "abcde"
map2_4 = "abzzz"


print(min_steps_to_match_maps(map1_1, map2_1))
print(min_steps_to_match_maps(map1_2, map2_2))
print(min_steps_to_match_maps(map1_3, map2_3))
print(min_steps_to_match_maps(map1_4, map2_4))
