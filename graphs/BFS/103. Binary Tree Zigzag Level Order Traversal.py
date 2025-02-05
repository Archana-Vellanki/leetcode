# 103. Binary Tree Zigzag Level Order Traversal
# Solved
# Medium
# Topics
# Companies
# Given the root of a binary tree, return the zigzag level order traversal of its nodes' values. (i.e., from left to right, then right to left for the next level and alternate between).

 

# Example 1:


# Input: root = [3,9,20,null,null,15,7]
# Output: [[3],[20,9],[15,7]]
# Example 2:

# Input: root = [1]
# Output: [[1]]
# Example 3:

# Input: root = []
# Output: []
 

# Constraints:

# The number of nodes in the tree is in the range [0, 2000].
# -100 <= Node.val <= 100

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# Have a boolean value to determine which side to start from. Modify the order in which elements are added to the temp list according to that boolean
# Time complexity: O(n)
# Space Complexity: O(n) because output contains all the nodes
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: 
            return []
        
        q = deque()
        q.append(root)
        result = []
        start_from_right = False
        while q:
            # print(q)
            size = len(q)
            
            temp = deque()
            for i in range(size):
                node = q.popleft()
                if start_from_right:
                    temp.appendleft(node.val)
                else:
                    temp.append(node.val)
                
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            result.append(list(temp))
            start_from_right = not start_from_right
            
        return result
