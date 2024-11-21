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

root = TreeNode(10)
leaf1 = TreeNode(10)

root.left = leaf1

print(check_root(root))

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