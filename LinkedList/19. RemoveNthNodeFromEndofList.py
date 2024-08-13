# 19.Remove Nth Node From End of List
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

# This approach uses two pointers, slow and fast, to find the nth node from the end of a linked list by maintaining 
# a gap of n nodes between them. Once fast reaches the end, slow points to the node just before the nth node, allowing the removal of the nth node by adjusting pointers.
# Time complexity: O(n)
# Space complexity: O(1)
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """

        if not head:
            return None
        
        slow = head
        fast = head
        counter = 0

        # print(slow.val, fast.val, '\n', counter)
        while fast.next:
            # This loop is to get n nodes between the fast and slow pointers. Because when fast node is at the end, 
            # slow pointer will be the previous node of the nth node from the end, which makes it the exact point where we have to modify the next pointer.
            if counter >= n:
                slow = slow.next
            fast = fast.next
            counter += 1
            # print(slow, fast, counter, '\n')
        if counter == n - 1:
            # This condition is to check if n is equal to the length of the LinkedList(number of nodes in it) and if so we have to remove the head node itself and can just return head.next as the new head.
            head = head.next
            return head
         
        slow.next = slow.next.next

        return head

        # Bruteforce approach:
        # Includes two traversals to find out number of nodes in the linkedlist in one traversal and then in the next traversal will iterate till the node at (length - n)position and then modify the next pointer.
        # Time complexity: O(2*n) = O(n)
        # Space complexity: O(1)
        

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
