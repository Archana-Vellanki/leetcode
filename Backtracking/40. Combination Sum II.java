/**
 * 40. Combination Sum II
 * Medium
 * 9.7K
 * 249
 * Companies
 * Given a collection of candidate numbers (candidates) and a target number
 * (target), find all unique combinations in candidates where the candidate
 * numbers sum to target.
 * 
 * Each number in candidates may only be used once in the combination.
 * 
 * Note: The solution set must not contain duplicate combinations.
 * 
 * 
 * 
 * Example 1:
 * 
 * Input: candidates = [10,1,2,7,6,1,5], target = 8
 * Output:
 * [
 * [1,1,6],
 * [1,2,5],
 * [1,7],
 * [2,6]
 * ]
 * Example 2:
 * 
 * Input: candidates = [2,5,2,1,2], target = 5
 * Output:
 * [
 * [1,2,2],
 * [5]
 * ]
 * 
 * 
 * Constraints:
 * 
 * 1 <= candidates.length <= 100
 * 1 <= candidates[i] <= 50
 * 1 <= target <= 30
 */

class Solution {
    public List<List<Integer>> combinationSum2(int[] candidates, int target) {
        Arrays.sort(candidates);
        List<List<Integer>> result = new ArrayList<>();
        backtrack(new ArrayList<Integer>(), 0, candidates, target, result);
        return result;
    }

    private void backtrack(ArrayList<Integer> currentList, int currIndex, int[] candidates, int target,
            List<List<Integer>> result) {
        int currSum = 0;
        for (int each : currentList) {
            currSum += each;
        }
        if (currSum == target) {
            result.add(new ArrayList<>(currentList));
        } else if (currSum > target) {
            return;
        }
        int size = currentList.size();
        for (int i = currIndex; i < candidates.length; i++) {
            if (currSum + candidates[i] <= target) {
                if (i > currIndex && candidates[i] == candidates[i - 1]) // eliminate duplicates
                    continue;
                currentList.add(candidates[i]);
                backtrack(currentList, i + 1, candidates, target, result); // as each element should be considered only
                                                                           // once => f(i+1)
                currentList.remove(size);
            } else
                break;
        }
    }
}