# 206. Reverse Linked List
# Solved
# Easy
# Topics
# Companies
# Given the head of a singly linked list, reverse the list, and return the reversed list.

 

# Example 1:


# Input: head = [1,2,3,4,5]
# Output: [5,4,3,2,1]
# Example 2:


# Input: head = [1,2]
# Output: [2,1]
# Example 3:

# Input: head = []
# Output: []
 

# Constraints:

# The number of nodes in the list is the range [0, 5000].
# -5000 <= Node.val <= 5000
 

# Follow up: A linked list can be reversed either iteratively or recursively. Could you implement both?

# Approach: keep track of a prevNode and nextNode to attach the node's next node to prev and prev to the current node and nextnode as the nextnode.next, there by reaching till the end.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = head
        if not head:
            return head
        prevNode, nextNode = None, node.next
        while nextNode:
            node.next = prevNode
            prevNode = node
            node = nextNode
            nextNode = nextNode.next
        node.next = prevNode
        return node
