# 101. Symmetric Tree
# Easy

# Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).


# Example 1:


# Input: root = [1,2,2,3,4,4,3]
# Output: true
# Example 2:


# Input: root = [1,2,2,null,3,null,3]
# Output: false


# Constraints:

# The number of nodes in the tree is in the range [1, 1000].
# -100 <= Node.val <= 100


# Follow up: Could you solve it both recursively and iteratively?

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        left = root.left
        right = root.right

        def childSymmetryCheck(left, right):
            print(left, right)
            if (right and not left) or (left and not right):
                return False
            elif not left and not right:
                return True
            elif left.val != right.val:
                return False
            return childSymmetryCheck(left.right, right.left) and childSymmetryCheck(left.left, right.right)

        return childSymmetryCheck(left, right)


# Iterative approach
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        left = root.left
        right = root.right

        stack = [(left, right)]

        while stack:
            left, right = stack.pop()
            if not right and not left:
                continue
            if not right or not left:
                return False
            if left.val != right.val:
                return False
            stack.append((left.left, right.right))
            stack.append((left.right, right.left))

        return True
