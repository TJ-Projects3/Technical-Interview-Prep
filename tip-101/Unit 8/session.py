class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def check_root(root):
    if root:
        if root.right and root.left:
            return root.right.val + root.left.val == root.val
            
        if root.right:
            return root.right.val == root.val 
                
        if root.left:
            return root.left.val == root.val
            
    return False

"""
Given the root of a binary tree, return a list representing the inorder traversal of its nodes' values.
In an inorder traversal we traverse the left subtree, then the current node, then the right subtree.

We are asked to perform an inorder traversal, which is a type of depth-first search. We visit the leftmost node then its root,
and then the right subtree of that root.
"""

def inorder_traversal(root):
    result = []

    def traverse(current): 
        if current:
            traverse(current.left)

            result.append(current.val)

            traverse(current.right)

    traverse(root)
    return result

root = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(5))

print(inorder_traversal(root))
"""
Given the root of a binary tree, write a function size() that returns the number of nodes in the binary tree.

Evaluate the time complexity of your function.

Understand, we are writing a function that visits each node and counts the # of nodes in the binary tree.
Plan, We will solve this problem using dfs to visit each node, and as we visit each node we will keep a count and iterate it
to get the binary tree's size. We will be using inorder traversal
"""
def size(root):
    if not root:
        return 0
    
    stack = [root]
    count = 0
    while stack:
        node = stack.pop()
        count += 1

        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    return count
    
print(size(root))

def tree_expression(root):
    if root.val == "AND":
        return root.left.val and root.right.val
    
    if root.val == "OR":
        return root.left.val or root.right.val


test = TreeNode("OR", TreeNode(False), TreeNode(True))

print(tree_expression(test))

def equality(root):
    # Return True if both children are equal. The tree has AT MOST 3 NODES
    if root.left and root.right:
        return root.left.val == root.right.val
    else:
        return False

root = TreeNode(0, TreeNode(1), TreeNode(2))

print(equality(root))


def left_path(root):
	# We will traverse the left subtree, if there is one and keep track of the path with
    # a list as we get to the leftmost node.
    result = []

    if not root:
        return None
    
    if not root.left:
        return [root.val]
    
    return [root.val] + left_path(root.left)


root = TreeNode('adam', TreeNode('bart', TreeNode(1), TreeNode(2)), TreeNode('charlie', None, TreeNode('d')))

print(left_path(root))

# Given the root of a binary tree, return a list representing the preorder traversal of its nodes' values. 
# In an preorder traversal we traverse the current node, then the left subtree, then the right subtree.

# # Example Input Tree: 
# """For example:
#       1
#      / \
#     /   \
#    2     5
#   / \    
#  4   3 
# """
# # Input: root = 1
# # Expected Output: [1,3,2]

# # Input: root = None
# # Output: []

# # Example Input Tree
# """ 1 """ 
# # Input: root = 1
# # Output: [1]

def preorder_traversal(root):
    result = []

    def pre_traverse(current):
        if current:
            result.append(current.val)
            
            pre_traverse(current.left)

            pre_traverse(current.right)
    
    pre_traverse(root)
    return result
            
    
    # right_tree = preorder_traversal(root.right)
    # left_tree = preorder_traversal(root.left)
    # return [root.val] + left_tree + right_tree

print(preorder_traversal(root))

# Given the root of a binary tree and a value val, write a function is_lesser() 
# that returns True if all the nodes in the tree have a value less than 
# val and False otherwise. If the tree is empty, return False.

# Evaluate the time complexity of your function.

def is_lesser(root, val):
    if root is None: # If tree is empty to begin with
        return False # return False
    
    if root.val >= val: # If root.val is greater than val
        return False # return False because all nodes should be
    # lesser than val
    
    if not root.right and not root.left: # If there are no children left
        return True # return True "early"
    
    return (True if not root.left else is_lesser(root.left, val) and 
           True if not root.right else is_lesser(root.right, val))
# Recursively check the left and right subtrees if there are children there
# if there are no children return True by default, this will be overwritten
# if there are ANY False at all
# It will return True if both subtrees are valid and have nodes lesser than
# the value parameter


root = TreeNode(1, TreeNode(2, TreeNode(1), TreeNode(2)), TreeNode(5, None, TreeNode(6)))

print(is_lesser(root, 8))

# # Given a value and the root of a binary tree, write a function contains_greater() which returns
# # True if any nodes greater than value exist in the tree. If no node greater 
# # than value exist, return False. Assume the tree is balanced.

# Evaluate the time complexity of your solution.

    
    
