/**
 * 78. Subsets
 * Medium
 * 16K
 * 234
 * Companies
 * Given an integer array nums of unique elements, return all possible
 * subsets
 * (the power set).
 * 
 * The solution set must not contain duplicate subsets. Return the solution in
 * any order.
 * 
 * 
 * 
 * Example 1:
 * 
 * Input: nums = [1,2,3]
 * Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
 * Example 2:
 * 
 * Input: nums = [0]
 * Output: [[],[0]]
 * 
 * 
 * Constraints:
 * 
 * 1 <= nums.length <= 10
 * -10 <= nums[i] <= 10
 * All the numbers of nums are unique.
 */

/**
 * Start with an empty list.
 * For each element, there are two choices: to consider or not to consider it.
 * For each list in the result array, keeping the existing lists as is, create a
 * new set of lists by adding the current element to all the pre-existing lists.
 * Add all the new lists to the result.
 * Return the result.
 */

class Solution {
    public List<List<Integer>> subsets(int[] nums) {
        List<List<Integer>> result = new ArrayList<>(1 << nums.length);
        result.add(Arrays.asList(new Integer[0]));
        for (int i = 0; i < nums.length; i++) {
            int size = result.size();
            for (int j = 0; j < size; j++) {
                List<Integer> curr = new ArrayList<>(result.get(j));
                curr.add(nums[i]);
                result.add(curr);
            }
        }
        return result;
    }
}