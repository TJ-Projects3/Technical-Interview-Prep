# Stacks, Queues, and Two Pointer Algorithm

# You are managing a social media platform and need to ensure that posts are properly formatted. 
# Each post must have balanced and correctly nested tags, such as () for mentions, [] for hashtags, and {} for links. 
# You are given a string representing a post's content, and your task is to determine if the tags in the post are correctly formatted.

# A post is considered valid if:
# Every opening tag has a corresponding closing tag of the same type.
# Tags are closed in the correct order.

def is_valid_post_format(posts):
    # Initialize stack and dictionary
    # Use dictionary of parenthesis to identify each one
    # If we see an open tag push it to the stack
    # If we see closing tag check if the stack is not empty and has an opening tag of the same type (DICTIONARY)
    # If yes, pop the opening tag from the stack
    # If no, we return False because the tags are organized correctly there should a open tag for the "corresponding" closing tag.
    # If the stack is empty at the end of the loop return True if not False
    stack = []
    dictionary = {")": "(", "}": "{", "]": "["}

    if len(posts) % 2 != 0: # If the length of posts is odd
        return False # It's false because each tag has a corresponding one, so there will pairs* of tags in each list meaning it will always be even.

    for i in posts: # For every bracket in posts
        if i in dictionary.values(): # If it is a opening tag # ({(
            stack.append(i) # Append it to the stack # stack: ({(
        
        elif i in dictionary.keys(): # } - True #
            if stack and dictionary[i] == stack[-1]: # True # stack: ({(
                stack.pop() # stack: ({
            else:
                return False
            
    return len(stack) == 0

print(is_valid_post_format("([])"))
print(is_valid_post_format("(()[]{})[[]]")) 
print(is_valid_post_format("]"))

# On your platform, comments on posts are displayed in the order they are received. However,
# for a special feature, you need to reverse the order of comments before displaying them. 
# Given a queue of comments represented as a list of strings, reverse the order using a stack.

# def reverse_comments_queue(comments):
  # Initialize a stack
  # For every comment in comments
  # push the comment to the stack
  # return the stack?
#     stack = []

#     for comment in comments:
#         stack.append(comment)
    
#     result = []

#     while stack:
#         result.append(stack.pop())
    
#     return result

# print(reverse_comments_queue(["Great post!", "Love it!", "Thanks for sharing."]))

# print(reverse_comments_queue(["First!", "Interesting read.", "Well written."]))

# You are given a list watchlist representing a list of shows sorted by popularity for a particular user. 
# The user wants to discover new shows they haven't heard of before by reversing the list to show the least popular shows first.
# Using the two-pointer approach, implement a function reverse_watchlist() that reverses the order of the watchlist in-place. 
# This means that the first show in the given list should become the last, the second show should become the second to last,
#  and so on. Return the reversed list. Do not use list slicing (e.g., watchlist[::-1]) to achieve this.

# Reverse the list using a two pointer approach so that this sorted list by least to most popularity becomes most to least.
# We will use two pointer (one at start and one at end) to simultaneously assign the first and last value to each other,
# then we increment the start and decrement the ending index to move onto the next two shows to be switched, and continue to do same
# thing until we reach the point where the pointers meet.

def reverse_watchlist(watchlist):
    left, right = 0, len(watchlist) - 1

    while left < right:
        watchlist[left], watchlist[right] = watchlist[right], watchlist[left]
        left += 1
        right -= 1
    return watchlist


# Example Usage:

watchlist = ["Breaking Bad", "Tester", "The Crown", "The Witcher", "Stranger Things"]

print(reverse_watchlist(watchlist))
  
# Example Output:

# ['The Witcher', 'The Crown', 'Stranger Things', 'Breaking Bad']
