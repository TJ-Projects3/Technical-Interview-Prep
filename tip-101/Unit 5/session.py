# class Pokemon():
# 	def  __init__(self, name, hp, damage):
# 		self.name = name
# 		self.hp = hp # hit points
# 		self.damage = damage # The amount of damage this pokemon does to its opponent every attack
		
# 	def attack(self, opponent):
# 		print(f"{opponent.name} health: {opponent.hp}")
# 		opponent.hp = opponent.hp - self.damage
# 		print(f"{self.name} dealt {self.damage} to {opponent.name}")
# 		print(f"{opponent.name} health: {opponent.hp}")

# pikachu = Pokemon("Pikachu", 35, 20)
# bulbasaur = Pokemon("Bulbasaur", 45, 30) 

# opponent = bulbasaur
# pikachu.attack(opponent)

# In the Player class below, each player has a race_outcomes attribute which holds a list of integers describing 
# what place they came in for each race in a tournament.

# Write a method get_tournament_place() that takes in one parameter opponents, a list of other player objects also 
# participating in the tournament, and returns the place in the overall tournament.

# Rank in the tournament is determined by the lowest average race outcome. (1st place is better than 2nd!)
# Each opponent in opponents is guaranteed to have participated in the same number of races as the current player.

class Player:
    def __init__(self, character, kart, outcomes):
        self.character = character
        self.kart = kart
        self.items = []
        self.race_outcomes = outcomes
        
	# Go through each opponent, use their outcomes list average to find out who had better placing by seeing who's is less

    def get_tournament_place(self, opponents):
        best_placing = sum(self.race_outcomes) / len(self.race_outcomes) # Do the initial object average
        placing = 1
        
        for racer in opponents:
              results = racer.race_outcomes
              average_place = sum(results) / len(results) # Do each opponent average
              if average_place < best_placing: # See if its better than the initial racers average
                    placing += 1 # If it is, the racers placing goes down
                    
        return placing
    
player1 = Player("Mario", "Standard", [1, 2, 1, 1, 3])
player2 = Player("Luigi", "Standard", [2, 1, 3, 2, 2])
player3 = Player("Peach", "Standard", [3, 3, 2, 3, 1])

opponents_one = [player2, player3]
print(f"{player1.character} was number {player1.get_tournament_place(opponents_one)}")

# Write a function add_second() that takes in the head of a linked list and a value object val as parameters. 
# It should insert val as the second node in the linked list and return the head of the linked list. (You can assume head is not None.)

# Note: The "head" of a linked list is the first element in the linked list. Equivalent to lst[0] of a normal list.

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next
        
	# We know we will traverse partially through the list to place the value.
    # It will be the second node, so right next to head, this is even more efficient
    # We could traverse but not necessary, we'll just do it in a different way for efficiency.
        
    def add_second(head, val):
         new_node = Node(val, head.next)
         head.next = new_node
         return head

    # Adding the node in-place at the second spot
	#  1 -> 2 -> 3
	# 	  4^
    # 1-> 4 -> 2 -> 3
    
    # Write a function increment_ll() that takes in the head of a linked list of integer values and 
    # returns the same list, but with each node's value incremented by 1. Return the head of the list.
    
	# We know that were going to traverse through the entire list
    # We will modify the values and increment them by one as we go
    # Then return the new modified list (head).

def increment_ll(head):
    current = head # list pointer
    while current:
        current.value = current.value + 1 # Increment by 1
        current = current.next
    return head

node3 = Node(5, None)              
node2 = Node(4, node3)
node1 = Node(3, node2)

print("Original:", node1.value)

node1 = increment_ll(node1)
# node1: 6 -> 7 -> 8
print("Incremented by 1:", node1.value)

node1 = increment_ll(node1)
# my_list: 7 -> 8 -> 9
print("Incremented by 1 a second time:", node1.value)
    

         

		