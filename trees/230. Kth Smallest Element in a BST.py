# 230. Kth Smallest Element in a BST
# Solved
# Medium
# Topics
# Companies
# Hint
# Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) of all the values of the nodes in the tree.

 

# Example 1:


# Input: root = [3,1,4,null,2], k = 1
# Output: 1
# Example 2:


# Input: root = [5,3,6,2,4,null,null,1], k = 3
# Output: 3
 

# Constraints:

# The number of nodes in the tree is n.
# 1 <= k <= n <= 104
# 0 <= Node.val <= 104
 

# Follow up: If the BST is modified often (i.e., we can do insert and delete operations) and you need to find the kth smallest frequently, how would you optimize?


# In order traversal.Keep a counter to track the number of nodes visited. once it reaches k it means that the current node is the kth smallest node.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if not root:
            return None
        counter = 0
        ans = None
        def inOrder(root):
            nonlocal counter
            nonlocal k
            nonlocal ans
            if not root or counter > k:
                return
            inOrder(root.left)
            counter += 1
            if counter == k:
                ans = root.val
                return 
            inOrder(root.right)
        inOrder(root)
        return ans
