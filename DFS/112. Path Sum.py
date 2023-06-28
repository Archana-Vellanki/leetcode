# 112. Path Sum

# Easy
# 8.5K
# 951
# Companies
# Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf path such that adding up all the values along the path equals targetSum.

# A leaf is a node with no children.


# Example 1:


# Input: root = [5, 4, 8, 11, null, 13, 4, 7, 2, null, null, null, 1], targetSum = 22
# Output: true
# Explanation: The root-to-leaf path with the target sum is shown.
# Example 2:


# Input: root = [1, 2, 3], targetSum = 5
# Output: false
# Explanation: There two root-to-leaf paths in the tree:
# (1 - -> 2): The sum is 3.
# (1 - -> 3): The sum is 4.
# There is no root-to-leaf path with sum = 5.
# Example 3:

# Input: root = [], targetSum = 0
# Output: false
# Explanation: Since the tree is empty, there are no root-to-leaf paths.


# Constraints:

# The number of nodes in the tree is in the range[0, 5000].
# -1000 <= Node.val <= 1000
# -1000 <= targetSum <= 1000

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: bool
        """

        # Time complexity: O(n)
        # Space complexity: O(1)
        # Approach: if the root is None, since there is no tree, ans would be False
        # if both left and right nodes are not None, return if either of the pathSum is equal to TargetSum, by subtracting the current Node value from the targetSum
        # if either is none, return if the other's pathSum is equal to targetSum
        # if both are None, it means it is the leaf node and check if the current value is equal to the targetSum
        if root is None:
            return False

        if root.right and root.left:
            return self.hasPathSum(root.left, targetSum - root.val) or self.hasPathSum(root.right, targetSum - root.val)
        elif root.left:
            return self.hasPathSum(root.left, targetSum - root.val)
        elif root.right:
            return self.hasPathSum(root.right, targetSum - root.val)
        else:
            return targetSum == root.val
