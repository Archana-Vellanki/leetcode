# Remove Nth Node From End of List
# Medium

# Given the head of a linked list, remove the nth node from the end of the list and return its head.


# Example 1:
# Input: head = [1,2,3,4,5], n = 2
# Output: [1,2,3,5]

# Example 2:
# Input: head = [1], n = 1
# Output: []

# Example 3:
# Input: head = [1,2], n = 1
# Output: [1]


# Constraints:

# The number of nodes in the list is sz.
# 1 <= sz <= 30
# 0 <= Node.val <= 100
# 1 <= n <= sz


# Follow up: Could you do this in one pass?

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        slow = head
        fast = head
        counter = 0

        # print(slow.val, fast.val, '\n', counter)
        while fast.next:
            if counter >= n:
                slow = slow.next
            fast = fast.next
            counter += 1
            # print(slow, fast, counter, '\n')
        if counter == n - 1:
            head = head.next
            return head
        if slow:
            slow.next = slow.next.next

        return head

        # bruteforce approach
        # includes two traversals
        # node = head
        # length = 0

        # while node:
        #     length += 1
        #     node = node.next

        # if length == n:
        #     return head.next

        # index = length - n
        # counter = 0

        # node = head
        # # print(head, length, index, node)
        # while counter < index - 1 and node:
        #     node = node.next
        #     counter += 1
        # # print('\n', node, '\n\n', head)
        # node.next = node.next.next
        # return head
