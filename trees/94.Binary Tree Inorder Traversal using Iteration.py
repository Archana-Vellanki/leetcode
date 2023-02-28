# 94. Binary Tree Inorder Traversal
# Easy

# Given the root of a binary tree, return the inorder traversal of its nodes' values.

# Example 1:


# Input: root = [1,null,2,3]
# Output: [1,3,2]
# Example 2:

# Input: root = []
# Output: []
# Example 3:

# Input: root = [1]
# Output: [1]


# Constraints:

# The number of nodes in the tree is in the range [0, 100].
# -100 <= Node.val <= 100


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """

        # using Iteration
        if not root:
            return []

        arr = []
        stack = []
        node = root

        while True:
            while node:
                stack.append(node)
                node = node.left

            if stack:
                node = stack.pop()
                arr.append(node.val)
                node = node.right
            else:
                break

        return arr
