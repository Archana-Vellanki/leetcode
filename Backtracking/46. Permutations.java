/*
 * 46. Permutations
 * Medium
 * 18.1K
 * 292
 * Companies
 * Given an array nums of distinct integers, return all the possible
 * permutations. You can return the answer in any order.
 * 
 * 
 * 
 * Example 1:
 * 
 * Input: nums = [1,2,3]
 * Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
 * Example 2:
 * 
 * Input: nums = [0,1]
 * Output: [[0,1],[1,0]]
 * Example 3:
 * 
 * Input: nums = [1]
 * Output: [[1]]
 * 
 * 
 * Constraints:
 * 
 * 1 <= nums.length <= 6
 * -10 <= nums[i] <= 10
 * All the integers of nums are unique.
 */

class Solution {
    public List<List<Integer>> permute(int[] nums) {
        List<List<Integer>> result = new ArrayList<>();
        backtrack(new ArrayList<Integer>(), nums, result, 0);
        return result;

    }

    private void backtrack(ArrayList<Integer> curr, int[] nums, List<List<Integer>> result, int currSize) {
        if (currSize == nums.length) {
            result.add(new ArrayList<>(curr));
            return;
        }
        for (int i = 0; i < nums.length; i++) {
            if (curr.contains(nums[i]))
                continue;
            curr.add(nums[i]);
            backtrack(curr, nums, result, currSize + 1);
            curr.remove(currSize);
        }
    }
}