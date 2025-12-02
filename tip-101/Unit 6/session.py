"""
The assignment statement to the head variable below creates the linked list Mario -> Luigi -> Wario. 
Break apart the assignment statement into multiple lines with one call to the Node constructor per line to recreate the list.
"""

class Node:
	def __init__(self, value, next=None):
		self.value = value
		self.next = next

head = Node("Mario", Node("Luigi", Node("Wario")))\

node_one = Node("Mario")
node_two = Node("Luigi")
node_three = Node("Wario")

node_one.next = node_two
node_two.next = node_three

"""
 Given the head of a linked list, find the max value within the linked list
 We have our linked list as our input
 We return a single max value through this function
 We can consider some values could be strings so we must make sure they are numeric
 Another edge case could be head == Empty or head is None. Same thing
 O(n) time and O(1) memory
 Just traversing through the list provided, nothing crazy.
"""

def find_max(head):
	greatest = 0
	if head is None:
		return None
	
	current = head
	
	while current:
		if current.value > greatest:
			greatest = current.value
		current = current.next
	return greatest


head = Node(1,Node(5,Node(6,Node(5,Node(2)))))

print(find_max(head))



# Helper function to print the linked list
def print_list(node):
    current = node
    while current:
        print(current.value, end=" -> " if current.next else "")
        current = current.next
    print()

# Function with a bug!
def remove_by_value(head, val):
    # Check if the list is empty
    if head is None:
        return head

    # If the node to be removed is the head of the list
    if head.value == val:
        return head.next

    # Initialize pointers
    current = head.next
    previous = head

    # Traverse the list to find the node to remove
    while current:
        if current.value == val:
            previous.next = current.next
            return head
        previous = current
        current = current.next

    # If no node was found with the value `val`, return the original head
    return head

head = (Node(1,Node(2,Node(3,Node(4)))))
print_list(remove_by_value(head,3))

"""
Write a function return_book() that accepts a string title and a dictionary library as parameters. 
library maps book titles to the number of copies the library currently has in stock. 
The function should increment the quantity of the book title in library by 1 and return the updated dictionary. 
If title is not in the library, then add it and set quantity to 1.
"""
# Understand: We are searching for a title in the library (dictionary) to return.
# If title is present in the dictionary already then we add 1 to its value. If the title isn't present, then
# we add it into the library dictionary.
# Plan: Iterate through a for loop, to see all the keys and which possibly matches with title being returned.
# if you find the title add one to its value. If you cannot find the title, create a new key with value 1.

# def return_book(title, library):
#     if title in library:
#         library[title] += 1
#     else:
#         library[title] = 1
#     return library

# library = {"The Hobbit": 2, "1984": 1, "The Great Gatsby": 4}

# updated_lib = return_book("1984", library)
# print(updated_lib)

# updated_lib = return_book("The Giver", library)
# print(updated_lib)

"""
Write a function dict_difference() that takes two dictionaries and returns a new dictionary 
that contains only the key-value pairs found exclusively in the first dictionary but not in the second.
"""
 
# def dict_difference(d1, d2):
#     d3 = {}
#     for val in d1:
#         if val not in d2:
#             d3[val] = d1[val]     
#     return d3

# d1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
# d2 = {'b': 2, 'd': 1}

# print(dict_difference(d1,d2))

# Given the head of a linked list, return a dictionary that maps each unique element in the list to its frequency.
# Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for why you believe your solution
# has the stated time and space complexity.
# Plan: We will traverse through each element in the linked list and append each value to res using res.get(i, 0) + 1 as we get there.


class Node:
	def __init__(self, value, next=None):
		self.value = value
		self.next = next

def frequency_map(head):
     res = {}
     current = head
     while current:
           res[current.value] = res.get(current.value, 0) + 1
           current = current.next
     return res

head_one = Node(1, Node( 2, Node(2, Node(3, Node(3, Node(1, Node(4)))))))
print(frequency_map(head_one))

# Understand: We want to delete the node of a linked list, given the value in the linked list.

def delete_node(head, val):
      temp_head = Node("Temp")
      temp_head.next = head

      previous = temp_head
      current = head
      while current:
            if current.value == val:
                previous.next = current.next

            previous = current
            current = current.next
      return temp_head.next

# We are returning the frequency of a specific value (given by val) in the linked list (given by head)
# We will traverse through the list and check all the values to see if they match with val, if they do
# we simply iterate a counter.

def count_element(head, val):
    count = 0
    current = head
    while current:
        if current.value == val:
                count += 1
        current = current.next
    return count

print("Frequency:", count_element(head_one, 4))
    
# Helper function to print the linked list
def print_list(node):
    current = node
    while current:
        print(current.value, end=" -> " if current.next else "")
        current = current.next
    print()


# I have a bug! 
def remove_tail(head):
    if head is None: # If the list is empty, return None
        return None
    if head.next is None: # If there's only one node, removing it leaves the list empty
        return None 
		
	# Start from the head and find the second-to-last node
    current = head
    while current.next.next: 
        current = current.next

    current.next = None # Remove the last node by setting second-to-last node to None
    return head

print_list(head_one)
remove_tail(head_one)
print_list(head_one)




    
