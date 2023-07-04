# 543. Diameter of Binary Tree
# Easy
# 11.7K
# 727
# Companies
# Given the root of a binary tree, return the length of the diameter of the tree.

# The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

# The length of a path between two nodes is represented by the number of edges between them.


# Example 1:


# Input: root = [1,2,3,4,5]
# Output: 3
# Explanation: 3 is the length of the path [4,2,1,3] or [5,2,1,3].
# Example 2:

# Input: root = [1,2]
# Output: 1


# Constraints:

# The number of nodes in the tree is in the range [1, 104].
# -100 <= Node.val <= 100

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# Time complexity: O(n)
# Space complexity: O(n)

# Approach: Height is the count of number of nodes but diameter is the count of number of edges between two nodes
# recursively find the height of each node in the bottom up approach and update the diameter at each step
# for a null node,both the diameter and the height would be 0
# for a leaf node, the diameter would be 0 because there are no edges but the height would be 1 because there is 1 node

#       3    for 3 here, the height would be 1 + max(height(left), height(right)) = 1 + max(1,1) = 2
#      / \      and diameter would be height(left) + height(right) since the diameter indicates the number of edges between the left and right nodes
#     2   4


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        def dfs(node):
            nonlocal diameter
            if node is None:
                return 0

            left = dfs(node.left) if node.left else 0
            right = dfs(node.right) if node.right else 0
            diameter = max(diameter, left + right)
            return 1 + max(left, right)

        diameter = 0
        dfs(root)
        return diameter
