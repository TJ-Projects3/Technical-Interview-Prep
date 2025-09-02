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

# def is_balanced(code): # Think like a human in real life for the problem
# # # Count the letters
# # # Have a copy
# # # Remove every letter once using a for loop to see which balances the string
# # Return T/F depending on if we can balance the string (all frequencies equal) by removing one letter.
#     count = {}
#     for i in code:
#         count[i] = count.get(i, 0) + 1

#     for i in count: # We want to loop through count because we wont waste time on duplicate letters
#         count_copy = count.copy()
#         count_copy[i] -= 1

#         if count_copy[i] == 0: # Remove the letter if it now equals 0, meaning it does not exist in the code anymore after removal
#             del count_copy[i] 
        
#         word_check = set(count_copy.values())

#         if len(word_check) == 1:
#             return True
#     return False



# code1 = "arghh"
# code2 = "haha"

# print(is_balanced(code1)) 
# print(is_balanced(code2)) 

# #     # returning True or False based off if we can balance the count by removing one letter
# #     # After counting, search for the greatest count and subtract it - 1



# # # Captain Feathersword and their crew has discovered a list of gold amounts at various hidden locations on an island. 
# # # Each number on the map corresponds to the amount of gold at a specific location. Captain Feathersword already has plenty of loot, 
# # # and their ship is nearly full. They want to find two distinct locations on the map such that the sum of the gold amounts at these 
# # # two locations is exactly equal to the amount of space left on their ship.

# # # Given an array of integers gold_amounts representing the amount of gold at each location and an integer target, 
# # # return the indices of the two locations whose gold amounts add up to the target.

# # # Assume that each input has exactly one solution, and you may not use the same location twice. You can return the answer in any order.

# # # This is a Two Sum solution
# # # We want to iterate through a for loop with an enumerate, and subtract the target - value of iterator to see if it exists in the list
# # # We can find out if it exists not using a list, but using the direct lookup of a hashmap, which is O(1) by the way
# # # We will subtract target - val each loop
# # # Remember, we want the indices...

# def find_treasure_indices(gold_amounts, target):
# #     # Hashmap
# #     # For loop
# #     # if target - val in the hashmap:
# #         # return [something, something] that add up to target
# #     # Regardless, keep assigning iterator value to its index.
#     res = {}
#     for i, val in enumerate(gold_amounts):
#         if target - val in res: # 9 - 2 = 7 F # 9 - 7 = 2 T
#             return [res[target - val], i] # i = 1, returns [1, 0]
#         res[val] = i # {2: 0}

# # gold_amounts1 = [2, 7, 11, 15]
# # target1 = 9

# # gold_amounts2 = [3, 2, 4]
# # target2 = 6

# # gold_amounts3 = [3, 3]
# # target3 = 6

# # print(find_treasure_indices(gold_amounts1, target1))  
# # print(find_treasure_indices(gold_amounts2, target2))  
# # print(find_treasure_indices(gold_amounts3, target3))


# # Problem 6: Organize the Pirate Crew
# # Captain Blackbeard needs to organize his pirate crew into different groups for a treasure hunt. Each pirate has a unique ID from 0 to n - 1.
# # You are given an integer array group_sizes, where group_sizes[i] is the size of the group that pirate i should be in.
# # For example, if group_sizes[1] = 3, then pirate 1 must be in a group of size 3.
# # Return a list of groups such that each pirate i is in a group of size group_sizes[i].
# # Each pirate should appear in exactly one group, and every pirate must be in a group. 
# # If there are multiple answers, return any of them. It is guaranteed that there will be at least one valid solution for the given input.

# # Based on the value, we will organize the indices into groups of those sizes.
# # Count the number of group sizes in hashmap

# def organize_pirate_crew(group_sizes):
#     group_tracker = {} # Initialize hashmap to track list of each group
#     for i in group_sizes: # For every group size in the given list
#         group_tracker[i] = [] # Mapping group size to list of pirates
#     result = []
#     for i, val in enumerate(group_sizes):
#         group_tracker[val].append(i) # Append the pirate ID from group_sizes into tracker list

#         if len(group_tracker[val]) == val: # If the tracker list is full for a group size
#             result.append(group_tracker[val]) # Append the current full group to the result list
#             group_tracker[val] = [] # Empty the list for space since one group has been organized and moved to result.
#     return result # Return the final result of organized, complete group lists

# # group_sizes1 = [3, 3, 3, 3, 3, 1, 3]
# # group_sizes2 = [2, 1, 3, 3, 3, 2]
# # group_sizes3 = [2, 2]
# # group_sizes4 = [2, 2, 1, 1, 1, 3, 3, 3]

# # print(organize_pirate_crew(group_sizes1))
# # print(organize_pirate_crew(group_sizes2))
# # print(organize_pirate_crew(group_sizes3))
# # print(organize_pirate_crew(group_sizes4))

# # Captain Blackbeard has two treasure maps represented by two strings of the same length map1 and map2. In one step, 
# # you can choose any character of map2 and replace it with another character.
# # Return the minimum number of steps to make map2 an anagram of map1.
# # An Anagram of a string is a string that contains the same characters with a different (or the same) ordering.

# def min_steps_to_match_maps(map1, map2):
#     if len(map1) != len(map2):
#         return None

#     counter1 = {}
#     counter2 = {}
#     diff_count = 0
    
#     for i, n in zip(map1, map2):
#         counter1[i] = counter1.get(i, 0) + 1
#         counter2[n] = counter2.get(n, 0) + 1

#     if counter1 == counter2:
#         return 0

#     for i in counter2:  # For every character in map2
#         if i in counter1: # If it's in map1
#             if counter2[i] > counter1[i]:
#                 diff_count += counter2[i] - counter1[i]
#         else:
#             diff_count += counter2[i]  # Add count for characters missing in counter1

#     return diff_count # Return total mismatching characters in "minimum steps"

# map1_1 = "bab"
# map2_1 = "aba"
# map1_2 = "treasure"
# map2_2 = "huntgold"
# map1_3 = "anagram"
# map2_3 = "mangaar"
# map1_4 = "abcde"
# map2_4 = "abzzz"


# print(min_steps_to_match_maps(map1_1, map2_1))
# print(min_steps_to_match_maps(map1_2, map2_2))
# print(min_steps_to_match_maps(map1_3, map2_3))
# print(min_steps_to_match_maps(map1_4, map2_4))


# # Problem 8: Counting Pirates' Action Minutes
# # Captain Dread is keeping track of the crew's activities using a log. 
# # The logs are represented by a 2D integer array logs where each logs[i] = [pirateID, time] indicates that the 
# # pirate with pirateID performed an action at the minute time. Multiple pirates can perform actions simultaneously, 
# # and a single pirate can perform multiple actions in the same minute. The pirate action minutes (PAM) for a given pirate is 
# # defined as the number of unique minutes in which the pirate performed an action. A minute can only be counted once, 
# # even if multiple actions occur during it.
# # You are to calculate a 1-indexed array answer of size k such that, for each j (1 <= j <= k), answer[j] is the number of pirates whose PAM equals j.

# # Return the array answer as described above.

# def counting_pirates_action_minutes(logs, k):
#     # Use a dictionary, and have a result list
#     # Map each pirateID to a set of times
#     # Before we do this, we check if the pirateID is already in the dictionary
#     # We do this because we are adding unique times to the set at the same time
#     # After we have the pirateID mapped to a set of unique times, the length of
#     # the set == the pirateID's PAM
#     # We will use len(pam_counter[j]) as our index, IF it <= k.
#     # We will iterate the count by one at the index as the list communicates
#     # The number of pirates with a specific PAM (value), with the PAM being measured
#     # by the index
#     pam_counter = {}
#     result = [0] * k

#     for i in range(len(logs)):
#         if logs[i][0] not in pam_counter:
#             pam_counter[logs[i][0]] = set()
#         pam_counter[logs[i][0]].add(logs[i][1])

#     for j in pam_counter:
#         if len(pam_counter[j]) <= k:
#             result[len(pam_counter[j]) - 1] += 1
    
#     return result

        
# logs1 = [[0, 5], [1, 2], [0, 2], [0, 5], [1, 3]]
# k1 = 5
# logs2 = [[1, 1], [2, 2], [2, 3]]
# k2 = 4

# print(counting_pirates_action_minutes(logs1, k1)) 
# print(counting_pirates_action_minutes(logs2, k2))


# As the curator of an art gallery, you are organizing a new exhibition. You must ensure the collection of art pieces are balanced to attract the 
# right range of buyers. A balanced collection is one where the difference between the maximum and minimum value of the art pieces is exactly 1.
# Given an integer array art_pieces representing the value of each art piece, write a function find_balanced_subsequence() 
# that returns the length of the longest balanced subsequence.

# A subsequence is a sequence derived from the array by deleting some or no elements without changing the order of the remaining elements.

# def find_balanced_subsequence(art_pieces):
#     # Use a dictionary to count occurences of each number
#     # For each art piece in the dictionary:
#     # if n + 1 exists in the dictionary
#     # max_length = max(0,dict[n]  + dict[n+1])
#     # return our answer max_length
#     count = {}
#     max_length = 0
#     for i in art_pieces:
#         count[i] = count.get(i, 0) + 1
    
#     for n in count:
#         if n + 1 in count:
#             max_length = max(max_length, count[n] + count[n+1])
#     return max_length
# art_pieces1 = [1,3,2,2,5,2,3,7]
# art_pieces2 = [1,2,3,4]
# art_pieces3 = [1,1,1,1]

# print(find_balanced_subsequence(art_pieces1))
# print(find_balanced_subsequence(art_pieces2))
# print(find_balanced_subsequence(art_pieces3))

# Imagine you are working on a wildlife conservation database. Write a function named most_endangered() 
# that returns the species with the highest conservation priority based on its population.
# The function should take in a list of dictionaries named species_list as a parameter. Each dictionary represents data associated with a species, 
# including its name, habitat, and wild population. The function should return the name of the species with the lowest population.

# If there are multiple species with the lowest population, return the species with the lowest index.

# def most_endangered(species_list):
#     most_endangered = species_list[0]

#     for i in species_list[1:]:
#         if  i["population"] < most_endangered["population"]:
#             most_endangered = i
#     return most_endangered["name"]

# species_list = [
#     {"name": "Amur Leopard",
#      "habitat": "Temperate forests",
#      "population": 84
#     },
#     {"name": "Javan Rhino",
#      "habitat": "Tropical forests",
#      "population": 72
#     },
#     {"name": "Vaquita",
#      "habitat": "Marine",
#      "population": 10
#     },
#     {"name": "Vacko",
#      "habitat": "Saharan Desert",
#      "population": 100
#     }
# ]

# print(most_endangered(species_list))

# # As part of conservation efforts, certain species are considered endangered and are represented by the string endangered_species. Each character in this string denotes a different endangered species. You also have a record of all observed species in a particular region, represented by the string observed_species. Each character in observed_species denotes a species observed in the region.

# # Your task is to determine how many instances of the observed species are also considered endangered.

# # Note: Species are case-sensitive, so "a" is considered a different species from "A".

# # Write a function to count the number of endangered species observed.

# def count_endangered_species(endangered_species, observed_species):
#     # Edge case: if theres no endangered species in observed at all.
#     # Count the number of observed species
#     counter = {}
#     count = 0
#     for i in observed_species:
#         counter[i] = counter.get(i,0) + 1
    
#     for i in counter:
#         if i in endangered_species:
#             count += counter[i]
#     return count
#     # In another loop, if the observed species is endangered
#         # iterate the count by how many species are observed
#     # return the count
# endangered_species1 = "aA"
# observed_species1 = "aAAbbbb"

# endangered_species2 = "z"
# observed_species2 = "ZZ"

# print(count_endangered_species(endangered_species1, observed_species1)) 
# print(count_endangered_species(endangered_species2, observed_species2))  

# # Your art gallery has just been shipped a new collection of numbered art pieces, and you need to verify their authenticity. 
# # The collection is considered "authentic" if it is a permutation of an array base[n].
# # The base[n] array is defined as [1, 2, ..., n - 1, n, n], meaning it is an array of length n + 1 containing the 
# # integers from 1 to n - 1 exactly once, and the integer n twice. For example, base[1] is [1, 1] and base[3] is [1, 2, 3, 3].

# # Write a function is_authentic_collection that accepts an array of integers art_pieces and returns True
# # if the given array is an authentic array, and otherwise returns False.

# # Note: A permutation of integers represents an arrangement of these numbers. For example [3, 2, 1] and [2, 1, 3] 
# # are both permutations of the series of numbers 1, 2, and 3.
# def is_authentic_collection(art_pieces):
#     # Sort the array
#     # Intitialize a set
#     # We should only see a duplicate at the end
#     # If we reach the end of the list without that duplicate at the end return false.
#     n = max(art_pieces)
#     if n + 1 != len(art_pieces): # Checks if this actually has the length of a permutation
#         return False # If not, return False
    
#     count = {} # Dictionary

#     for i in art_pieces:
#         count[i] = count.get(i,0) + 1 # Count the art pieces

#     for i in range(1, n):
#         if count.get(i,0) != 1:
#             return False
        
#     return count.get(n, 0) == 2






# collection1 = [2, 1, 3]
# collection2 = [1, 3, 3, 2, 2]
# collection3 = [0,0, 1, 1]

# print(is_authentic_collection(collection1))
# print(is_authentic_collection(collection2))
# print(is_authentic_collection(collection3))

# You are tasked with organizing a collection of art prints represented by a list of strings collection. 
# You need to display these prints on a single wall in a 2D array format that meets the following criteria:
# - The 2D array should contain only the elements of the array collection.
# - Each row in the 2D array should contain distinct strings.
# - The number of rows in the 2D array should be minimal.
# Return the resulting array. If there are multiple answers, return any of them. 
# Note that the 2D array can have a different number of elements on each row.

# def organize_exhibition(collection):
#     # Use a set to solve this problem
#     # Have our 2D list
#     # We'll add values into the set until we get a value that's already in the set.
#     # After we get that, we'll append a list of our set to the array.
#     # The set will be emptied after this and we'll keep doing this for the rest

#     # Greedy Method
#     # For each row start with an empty row
#     # Try to place as many prints as possible inside that row
#     # Once you cannot add to the row, start a new row
#     # Keep going and so on
    
#     # result
#     result = []
#     # copy of collection so that we can modify accordingly and track the remaining elements
#     art_remaining = collection.copy()
#     # while collection.copy reamins
#     while art_remaining:
#         # create a new row for each
#         current_list = []
#         # Track the unique elements through the set
#         unique_strings = set()
#         # We have 2 options: initialize a pointer or loop through another copy so that you dont get an index error.
#         # Loop through another copy
#         for i in art_remaining.copy():
#         # If the value is not in the set, add it to the current row, add it to the set to be tracked, and remove it from collection.copy()
#             if i not in unique_strings:
#                 unique_strings.add(i)
#                 current_list.append(i)
#                 art_remaining.remove(i)
#             # After the if condition, add the row to the result
#         result.append(current_list)
#         # Out of the loop, return result.
#     return result

# collection1 = ["O'Keefe", "Kahlo", "Picasso", "O'Keefe", "Warhol", 
#               "Kahlo", "O'Keefe"]
# collection2 = ["Kusama", "Monet", "Ofili", "Banksy"]

# print(organize_exhibition(collection1))
# print(organize_exhibition(collection2))

# Your gallery has been trying to increase it's online presence by hosting several virtual galleries. Each virtual gallery's web 
# traffic is tracked through domain names, where each domain may have subdomains.

# A domain like "modern.artmuseum.com" consists of various subdomains. At the top level, we have "com", at the next level, we have "artmuseum.com", 
# and at the lowest level, "modern.artmuseum.com". When visitors access a domain like "modern.artmuseum.com", they also implicitly
# visit the parent domains "artmuseum.com" and "com". A count-paired domain is represented as "rep d1.d2.d3" where rep is the number of visits 
# to the domain and d1.d2.d3 is the domain itself. For example, "9001 modern.artmuseum.com" indicates that "modern.artmuseum.com" was visited 9001 times.
# Given an array of count-paired domains cpdomains, return an array of the count-paired domains of each subdomain. The order of the output does not matter.

# def subdomain_visits(cpdomains):
#     # Res hashmap
#     res = {}
#     # For every domain in cpdomains
#     for domain in cpdomains:
#         # Split the view count and domain by the space between them
#         view_count, address = domain.split(" ")
#         # Assign domain to key and view count to value
#         # Take each part of the domain by splitting the split domain again by the dots
#         dots_split = address.split(".")
#         # For every split dot domain
#         for i in range(len(dots_split)):
#             subdomain = '.'.join(dots_split[i:])
#             res[subdomain] = res.get(subdomain, 0) + int(view_count)
    
#     result = []
#     for key, val in res.items():
#         result.append(f"{val} {key}")

#     return result
#         # Join each subdomain and assigning it to a variable by going in reverse iterated order each iteration (.com -> arts.com -> gov.arts.com)
#         # Use subdomain as the key and iterate the current split string view count to its CURRENT VALUE
#         # Return each item in a list using res.items()

# cpdomains1 = ["9001 modern.artmuseum.com"]
# cpdomains2 = ["900 abstract.gallery.com", "50 impressionism.com", 
#               "1 contemporary.gallery.com", "5 medieval.org"]

# print(subdomain_visits(cpdomains1))
# print(subdomain_visits(cpdomains2))

# As a time traveling linguist, you are analyzing texts written in an ancient script. However, some words in 
# the text are illegible and can't be deciphered. Write a function find_most_frequent_word() that accepts a string
# text and a list of illegible words illegibles and returns the most frequent word in text that is not an illegible word.

# We will use a dictionary to find the frequencies of the words, but before that we will switch all the letters to lowercase, to ensure we count
# same letters.
# We count the letters while checking that i is not in ineligibles
# BEFORE ANYTHING we will have to clean the string using a for loop, we will check if the letter is a space or if it is alnum, if not we
# want to strip that character. After cleaning, we will split each word into a list by their characters
# This should be safe to view the max frequency now, use a for loop and everytime you see a new max update a variable max_key to the key of that new
# max value.
def find_most_frequent_word(text, illegibles):
    count = {}
    sentence = ""
    max_num, max_key = float('-inf'), ""
    for char in text:
        if char.isalpha() or char == " ":
            sentence += char.lower()

    for i in sentence.split(" "):
        if i not in illegibles:
            count[i] = count.get(i, 0) + 1
    
    for key in count:
        if count[key] > max_num:
            max_num = count[key]
            max_key = key
    return max_key

paragraph1 = "a."
illegibles1 = []
print(find_most_frequent_word(paragraph1, illegibles1)) 

paragraph2 = "Bob hit a ball, the hit BALL flew far after it was hit."
illegibles2 = ["hit"]
print(find_most_frequent_word(paragraph2, illegibles2)) 


    
