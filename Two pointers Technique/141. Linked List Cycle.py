# 141. Linked List Cycle
# Easy
# 12.6K
# 1K
# Companies
# Given head, the head of a linked list, determine if the linked list has a cycle in it.

# There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

# Return true if there is a cycle in the linked list. Otherwise, return false.


# Example 1:

# Input: head = [3, 2, 0, -4], pos = 1
# Output: true
# Explanation: There is a cycle in the linked list, where the tail connects to the 1st node(0-indexed).
# Example 2:


# Input: head = [1, 2], pos = 0
# Output: true
# Explanation: There is a cycle in the linked list, where the tail connects to the 0th node.
# Example 3:


# Input: head = [1], pos = -1
# Output: false
# Explanation: There is no cycle in the linked list.


# Constraints:

# The number of the nodes in the list is in the range[0, 104].
# -105 <= Node.val <= 105
# pos is -1 or a valid index in the linked-list.

# Follow up: Can you solve it using O(1)(i.e. constant) memory?

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


# Time Complexity: O(n)
# Space complexity: O(1)
# Approach: maintain a fast and a slow pointer. the fast moves two steps everytime and slow pointer moves just 1 step.
# check if the fast and slow pointers are referring to the same node. if Yes return True.
# If not, the loop ends since there is no next pointer. then return False

# Logic: if there is a cycle, the slow and fast pointers will definitely meet at some point. Example: hours and minutes hands in a clock.

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head:
            return False
        slow, fast = head, head.next

        while fast and fast.next:
            if fast == slow:
                return True
            fast = fast.next.next
            slow = slow.next
        return False


# Time Complexity: O(n)
# Space complexity: O(n)
# Approach: maintain a set to note the visited nodes. Iterate through the list and check the set to see if we have already visited the current node, if so return True.
# if the iteration is over and we couldnt find any repeated node, return False since there is no cycle in the list.
class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head:
            return False
        nodes = set()
        node = head
        while node.next:
            if node in nodes:
                return True
            nodes.add(node)
            node = node.next
        return False
