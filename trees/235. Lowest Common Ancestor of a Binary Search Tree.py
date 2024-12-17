# 235. Lowest Common Ancestor of a Binary Search Tree
# Solved
# Medium
# Topics
# Companies
# Given a binary search tree (BST), find the lowest common ancestor (LCA) node of two given nodes in the BST.

# According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

 

# Example 1:


# Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
# Output: 6
# Explanation: The LCA of nodes 2 and 8 is 6.
# Example 2:


# Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
# Output: 2
# Explanation: The LCA of nodes 2 and 4 is 2, since a node can be a descendant of itself according to the LCA definition.
# Example 3:

# Input: root = [2,1], p = 2, q = 1
# Output: 2
 

# Constraints:

# The number of nodes in the tree is in the range [2, 105].
# -109 <= Node.val <= 109
# All Node.val are unique.
# p != q
# p and q will exist in the BST.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# Approach1: To get common ancestors, first we need to store the ancestors of p then compare thwm with that of q. 
# Instead of using 2 lists for p and q's ancestors, I thought of using one queue for p's ancestors and  while traversing for q, I will pop as long as the ancestor is common.
# and keep updating the common ancestor. When I come across an ancestor which is not common, then I will break and return the latest common ancestor.
# There is a better approach 
# Time complexity: O(logn)
# Space complexity: O(logn)

# Approach2: Instead of using a list for storing the ancestors why dont we utilize the property of a BST which states that left < root< right. 
# So based on the values of p and q traverse through the tree and the node from which the two nodes start to be on the opposite sides, is the common ancestor.
# For example: 
#       8
#      /  \
#     4    12
#    / \   / \
#   2   6 9   14
# consider p=2 and q=6, 
# step1: 2< 8 and 6 < 8 ==> so both on the left side, node = node.left
# step2: 2 < 4 and 6 > 4 ==> so they are on different sides of 4. Hence its the lowest common ancestor.

# Time complexity: O(logn)
# Space complexity: O(1)


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # anc = None
        node = root
        while node:
            if p.val < node.val and q.val <node.val:
                # anc = node
                node = node.left
            elif p.val > node.val and q.val >node.val:
                # anc = node
                node = node.right
            else:
                # anc = node
                break
        return node
