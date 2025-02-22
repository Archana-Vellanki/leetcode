# 102. Binary Tree Level Order Traversal
# Medium

# Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).


# Example 1:


# Input: root = [3,9,20,null,null,15,7]
# Output: [[3],[9,20],[15,7]]
# Example 2:

# Input: root = [1]
# Output: [[1]]
# Example 3:

# Input: root = []
# Output: []

# Constraints:

# The number of nodes in the tree is in the range [0, 2000].
# -1000 <= Node.val <= 1000

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Time complexity: O(N)
# Space complexity: O(N)

# Approach:
# The solution maintains a queue for the traversal,
# in each iteration,
# initialize a list to store the values of all the nodes in the current level
# note the current size of the queue  as levelSize, to know the number of nodes in the current level.
# traverse through levelSize number of nodes in the queue to complete the entire level and append their values to the list
# add the child nodes(left and right) of the current node to the queue, which will be traversed in the next iteration
# at the end of the outer loop iteration, add the list to the traversal list

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        traversalList = []
        que = []
        que.append(root)

        while que:
            trvrsl = []
            for i in range(len(que)):
                node = que.pop(0)
                trvrsl.append(node.val)
                if node.left:
                    que.append(node.left)
                if node.right:
                    que.append(node.right)
            traversalList.append(trvrsl)
        return traversalList

# recursion
# pass level as a parameter to the recursive function call
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        result = []
        def levelOrder(node, level):
            if level < len(result):
                result[level].append(node.val)
            else:
                result.append([node.val])
            if node.left:
                levelOrder(node.left, level+1)
            if node.right:
                levelOrder(node.right, level+1)
        
        levelOrder(root, 0)
        
        return result
