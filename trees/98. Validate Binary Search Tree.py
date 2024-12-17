# 98. Validate Binary Search Tree
# Solved
# Medium
# Topics
# Companies
# Given the root of a binary tree, determine if it is a valid binary search tree (BST).

# A valid BST is defined as follows:

# The left 
# subtree
#  of a node contains only nodes with keys less than the node's key.
# The right subtree of a node contains only nodes with keys greater than the node's key.
# Both the left and right subtrees must also be binary search trees.
 

# Example 1:


# Input: root = [2,1,3]
# Output: true
# Example 2:


# Input: root = [5,1,4,null,null,3,6]
# Output: false
# Explanation: The root node's value is 5 but its right child's value is 4.
 

# Constraints:

# The number of nodes in the tree is in the range [1, 104].
# -231 <= Node.val <= 231 - 1

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Approach: Maintain the leftLimit and rightLimit values to check if every node is within the boundaries. Just checking the parent node is not enough, it should be between the proper limits.

class Solution:
    def isValidBST(self, root: Optional[TreeNode], leftLimit=float("-inf"), rightLimit = float("inf")) -> bool:
        if not root:
            return True
        elif not root.left and not root.right:
            return leftLimit < root.val < rightLimit
        elif not root.left:
            return root.val < root.right.val and leftLimit < root.val < rightLimit and self.isValidBST(root.right, root.val, rightLimit)
        elif not root.right:
            return root.val > root.left.val and leftLimit < root.val < rightLimit and self.isValidBST(root.left,leftLimit,root.val)
        else:
            return root.left.val < root.val < root.right.val and leftLimit < root.val < rightLimit and self.isValidBST(root.right,root.val,rightLimit) and self.isValidBST(root.left,leftLimit,root.val)
