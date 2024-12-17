# 110. Balanced Binary Tree
# Solved
# Easy
# Topics
# Companies
# Given a binary tree, determine if it is 
# height-balanced
# .

 

# Example 1:


# Input: root = [3,9,20,null,null,15,7]
# Output: true
# Example 2:


# Input: root = [1,2,2,3,3,null,null,4,4]
# Output: false
# Example 3:

# Input: root = []
# Output: true
 

# Constraints:

# The number of nodes in the tree is in the range [0, 5000].
# -104 <= Node.val <= 104

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        heights = {}
        def height(node) -> int:
            if not node:
                return 0
            if node in heights:
                return heights[node]
            heights[node] = 1 + max(height(node.left), height(node.right))
            return heights[node]
            

        lh, rh = height(root.left), height(root.right)
        # print(root.val, lh, rh)
        return self.isBalanced(root.left) and self.isBalanced(root.right) and abs(lh - rh) <= 1

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root == None:
            return True
        self.flag = True

        def height(root, ht = 0):
            if root == None:
                return ht
            
            left = height(root.left, ht + 1)
            right = height(root.right, ht + 1)
            if abs(left - right) > 1:
                self.flag = False
            return max(left, right)
        
        left = height(root.left)
        right = height(root.right)
        

        # if abs(left - right) > 1:
        #     return False
        return abs(left - right) <= 1 and self.flag
