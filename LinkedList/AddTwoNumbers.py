# 2. Add Two Numbers
# Medium

# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.


# Example 1:


# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]
# Explanation: 342 + 465 = 807.
# Example 2:

# Input: l1 = [0], l2 = [0]
# Output: [0]
# Example 3:

# Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
# Output: [8,9,9,9,0,0,0,1]


# Constraints:

# The number of nodes in each linked list is in the range [1, 100].
# 0 <= Node.val <= 9
# It is guaranteed that the list represents a number that does not have leading zeros.

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carry, result, temp = 0, 0, 0
        resultNode = None

        while (l1 or l2 or carry):

            a = l1.val if l1 else 0
            b = l2.val if l2 else 0

            tempSum = a + b + carry
            temp = tempSum % 10
            carry = tempSum//10
            result = result * 10 + temp
            # print(resultNode)
            if resultNode:
                resultNode.next = ListNode(temp, None)
                resultNode = resultNode.next
            else:
                resultNode = ListNode(temp, None)
                tempNode = resultNode
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            # print(result)
        return tempNode
