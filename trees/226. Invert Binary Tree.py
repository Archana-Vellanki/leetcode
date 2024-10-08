# 226. Invert Binary Tree
# Solved
# Easy
# Topics
# Companies
# Given the root of a binary tree, invert the tree, and return its root.

# Example 1:


# Input: root = [4,2,7,1,3,6,9]
# Output: [4,7,2,9,6,3,1]
# Example 2:


# Input: root = [2,1,3]
# Output: [2,3,1]
# Example 3:

# Input: root = []
# Output: []
 

# Constraints:

# The number of nodes in the tree is in the range [0, 100].
# -100 <= Node.val <= 100

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# recursive approach

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        temp = root.left
        root.left = self.invertTree(root.right)
        root.right = self.invertTree(temp)        
        return root

# iterative approach
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        myStack = [root]
        
        while myStack:
            currNode = myStack.pop()
            if currNode.left:
                myStack.append(currNode.left)
            if currNode.right:
                myStack.append(currNode.right)
            currNode.left, currNode.right = currNode.right, currNode.left

        return root
  
