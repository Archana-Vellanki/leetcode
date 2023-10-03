/*21. Merge Two Sorted Lists
Easy
20.1K
1.9K
Companies
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

 

Example 1:


Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]
Example 2:

Input: list1 = [], list2 = []
Output: []
Example 3:

Input: list1 = [], list2 = [0]
Output: [0]
 

Constraints:

The number of nodes in both lists is in the range [0, 50].
-100 <= Node.val <= 100
Both list1 and list2 are sorted in non-decreasing order.
 */

/**
 * Definition for singly-linked list.
 * public class ListNode {
 * int val;
 * ListNode next;
 * ListNode() {}
 * ListNode(int val) { this.val = val; }
 * ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */

/*
 * Initialize Two pointers indicating the curr nodes, increment the node which
 * has the lower value till we reach the end of one of the lists.
 * Append the other Linked List's nodes to the result directly
 */
class Solution {
    public ListNode mergeTwoLists(ListNode list1, ListNode list2) {
        ListNode one = list1;
        ListNode two = list2;
        ListNode curr = new ListNode();
        ListNode head = curr;

        while (one != null && two != null) {
            if (one.val > two.val) {
                curr.next = new ListNode(two.val);
                two = two.next;
            } else {
                curr.next = new ListNode(one.val);
                one = one.next;
            }
            curr = curr.next;
        }

        while (one != null) {
            curr.next = new ListNode(one.val);
            one = one.next;
            curr = curr.next;
        }
        while (two != null) {
            curr.next = new ListNode(two.val);
            two = two.next;
            curr = curr.next;
        }
        return head.next;
    }
}