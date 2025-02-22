# 144. Binary Tree Preorder Traversal
# Solved
# Easy
# Topics
# Companies
# Given the root of a binary tree, return the preorder traversal of its nodes' values.

 

# Example 1:

# Input: root = [1,null,2,3]

# Output: [1,2,3]

# Explanation:



# Example 2:

# Input: root = [1,2,3,4,5,null,8,null,null,6,7,9]

# Output: [1,2,4,5,6,7,3,8,9]

# Explanation:



# Example 3:

# Input: root = []

# Output: []

# Example 4:

# Input: root = [1]

# Output: [1]

 

# Constraints:

# The number of nodes in the tree is in the range [0, 100].
# -100 <= Node.val <= 100
 

# Follow up: Recursive solution is trivial, could you do it iteratively?

# Recursive:
# add current node to result. then recursively call the function for left subtree and right subtree
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        result = []
        def preOrder(node):
            if not node:
                return
            result.append(node.val)
            preOrder(node.left)
            preOrder(node.right)
        preOrder(root)
        return result

# Iterative
# For every node, we will add it to the result first.
# since stack pops the last node entered first, we will add right node followed by left node.

class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        node = root
        stack = [node]
        result = []
        while stack:
            popped = stack.pop()
            result.append(popped.val)
            if popped.right:
                stack.append(popped.right)
            if popped.left:
                stack.append(popped.left)
            
        return result
