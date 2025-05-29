# 653. Two Sum IV - Input is a BST
# Solved
# Easy
# Topics
# premium lock icon
# Companies
# Given the root of a binary search tree and an integer k, return true if there exist two elements in the BST such that their sum is equal to k, or false otherwise.

 

# Example 1:


# Input: root = [5,3,6,2,4,null,7], k = 9
# Output: true
# Example 2:


# Input: root = [5,3,6,2,4,null,7], k = 28
# Output: false
 

# Constraints:

# The number of nodes in the tree is in the range [1, 104].
# -104 <= Node.val <= 104
# root is guaranteed to be a valid binary search tree.
# -105 <= k <= 105


# Time Complexity: O(n)
# Space Complexity: O(n)

# Approach 1:
# inorder traversal and two sum on top of it
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        inorder = []
        stack = []
        curr = root
        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            inorder.append(curr.val)
            curr = curr.right

            
        left = 0
        right = len(inorder) - 1
        while left < right:
            currSum = inorder[left] + inorder[right]
            if currSum == k:
                return True
            elif currSum < k:
                left += 1
            else:
                right -= 1
        return False

# Approach 2:
# Same complexity as Approach 1
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        nums = set()
        q = [root]
        while q:
            curr = q.pop()
            if k - curr.val in nums:
                return True
            nums.add(curr.val)
            if curr.left:
                q.append(curr.left)
            if curr.right:
                q.append(curr.right)
        return False


        
# Approach 3:
# There is a better approach with space complexity of O(h) where he is the height of the binary tree. but its very complex.


