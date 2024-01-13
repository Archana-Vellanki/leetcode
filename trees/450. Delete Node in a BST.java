/**
 * 450. Delete Node in a BST

Given a root node reference of a BST and a key, delete the node with the given key in the BST. Return the root node reference (possibly updated) of the BST.

Basically, the deletion can be divided into two stages:

Search for a node to remove.
If the node is found, delete the node.
 

Example 1:


Input: root = [5,3,6,2,4,null,7], key = 3
Output: [5,4,6,2,null,null,7]
Explanation: Given key to delete is 3. So we find the node with value 3 and delete it.
One valid answer is [5,4,6,2,null,null,7], shown in the above BST.
Please notice that another valid answer is [5,2,6,null,4,null,7] and it's also accepted.

Example 2:

Input: root = [5,3,6,2,4,null,7], key = 0
Output: [5,3,6,2,4,null,7]
Explanation: The tree does not contain a node with value = 0.
Example 3:

Input: root = [], key = 0
Output: []
 

Constraints:

The number of nodes in the tree is in the range [0, 104].
-105 <= Node.val <= 105
Each node has a unique value.
root is a valid binary search tree.
-105 <= key <= 105
 

Follow up: Could you solve it with time complexity O(height of tree)?
 */

/**
 * Definition for a binary tree node.
 * public class TreeNode {
 * int val;
 * TreeNode left;
 * TreeNode right;
 * TreeNode() {}
 * TreeNode(int val) { this.val = val; }
 * TreeNode(int val, TreeNode left, TreeNode right) {
 * this.val = val;
 * this.left = left;
 * this.right = right;
 * }
 * }
 */
// Approach:
// Part 1: finding the node that has the value
// Part 2: deleting that node
// Once the node containing the value is found, we need the in-order successor
// to replace the current node.
// Get the left most node in the right sub-tree. Replace the current node's
// value with the successor's value. Then delete the successor node.
// (For deleting the successor node, call the same function with right sub-tree
// and successor's value as the parameters) and assign the result to the node's
// right subtree.
// Time Complexity: O(h) height of the tree
// Space complexity: O(h) height of the tree
class Solution {
    public TreeNode deleteNode(TreeNode root, int key) {
        if (root == null) {
            return null;
        }
        if (key < root.val) {
            root.left = deleteNode(root.left, key);
            // return root;
        } else if (key > root.val) {
            root.right = deleteNode(root.right, key);
            // return root;
        } else {
            if (root.left == null) {
                // left child is null so only child is to the right
                return root.right;
            } else if (root.right == null) {
                // right child is null so only child is to the left
                return root.left;
            } else {
                // both children are not null
                // TreeNode s_parent = root;
                TreeNode successor = root.right;
                while (successor.left != null) {
                    // s_parent = successor;
                    successor = successor.left;
                }
                // if (s_parent == root) {
                // s_parent.right = successor.right;
                // } else {
                // s_parent.left = successor.right;
                // }
                root.val = successor.val;
                root.right = deleteNode(root.right, successor.val);

            }
        }
        return root;
    }
}