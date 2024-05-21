# 23. Merge k Sorted Lists
# Solved
# Hard
# Topics
# Companies
# You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

# Merge all the linked-lists into one sorted linked-list and return it.


# Example 1:

# Input: lists = [[1,4,5],[1,3,4],[2,6]]
# Output: [1,1,2,3,4,4,5,6]
# Explanation: The linked-lists are:
# [
#   1->4->5,
#   1->3->4,
#   2->6
# ]
# merging them into one sorted list:
# 1->1->2->3->4->4->5->6
# Example 2:

# Input: lists = []
# Output: []
# Example 3:

# Input: lists = [[]]
# Output: []


# Constraints:

# k == lists.length
# 0 <= k <= 104
# 0 <= lists[i].length <= 500
# -104 <= lists[i][j] <= 104
# lists[i] is sorted in ascending order.
# The sum of lists[i].length will not exceed 104.

# Approach: Add all the first elements of the linkedlists to the heap, along with the index of the linkedlist in lists and the node,
# because we would need node to access the next element.
# If we add just the node, it would throw an error saying that there is no comparator for comparing listnodes

# Time Complexity:O(k) + O(nklogk) where n is number of elements in each list.
# Space complexity: O(n*k)

import heapq
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        result_head = ListNode()
        current = result_head
        k = len(lists)
        heap = []
        for i in range(k):
            if lists[i]:
                heapq.heappush(heap, (lists[i].val, i, lists[i]))
        # heapq.heapify(heap)
        # n = k
        while heap:  # loop runs for total number of elements which is nk
            popped_val, i, popped_node = heapq.heappop(heap)  # logk
            current.next = popped_node
            current = current.next
            # result_head.append(popped_val)
            if popped_node.next:
                heapq.heappush(
                    heap, (popped_node.next.val, i, popped_node.next))  # logk
        return result_head.next
