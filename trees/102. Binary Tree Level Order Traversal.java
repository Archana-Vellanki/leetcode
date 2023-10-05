/**
 * 102. Binary Tree Level Order Traversal
 * Medium
 * 14.4K
 * 287
 * Companies
 * Given the root of a binary tree, return the level order traversal of its
 * nodes' values. (i.e., from left to right, level by level).
 * 
 * 
 * Example 1:
 * 
 * 
 * Input: root = [3,9,20,null,null,15,7]
 * Output: [[3],[9,20],[15,7]]
 * Example 2:
 * 
 * Input: root = [1]
 * Output: [[1]]
 * Example 3:
 * 
 * Input: root = []
 * Output: []
 * 
 * 
 * Constraints:
 * 
 * The number of nodes in the tree is in the range [0, 2000].
 * -1000 <= Node.val <= 1000
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

/**
 * If the root is null, return empty List.
 * Maintain a queue to traverse through the nodes. add the root to the queue.
 * Iterate through the queue while it is not empty.
 * In each iteration, maintain a levelValues list to store the values in the
 * current level and the size of the queue to get the number of nodes in the
 * current level.
 * Start another loop to iterate through the current level nodes only.
 * As you Iterate through each node in the current level, add the value to the
 * levelValues list and
 * add the left and right nodes of the current node to the queue to be taken in
 * the next level.
 * Once the current level is done, add the levelValues to the result and proceed
 * with next level
 */
class Solution {
    public List<List<Integer>> levelOrder(TreeNode root) {
        if (root == null) {
            return (new ArrayList<>());
        }
        List<List<Integer>> res = new ArrayList<>();
        Queue q = new LinkedList<>();
        q.add(root);

        while (!q.isEmpty()) {
            int levelSize = q.size();
            List<Integer> levelValues = new ArrayList<>();

            for (int i = 0; i < levelSize; i++) {
                TreeNode curr = (TreeNode) q.poll();
                levelValues.add(curr.val);

                if (curr.left != null) {
                    q.add(curr.left);
                }
                if (curr.right != null) {
                    q.add(curr.right);
                }
            }
            res.add(levelValues);
        }
        return res;
    }

}