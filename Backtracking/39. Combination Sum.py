# 39. Combination Sum
# Medium
# 16.6K
# 335
# Companies
# Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. 
# You may return the combinations in any order.

# The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the 
# frequency
#  of at least one of the chosen numbers is different.

# The test cases are generated such that the number of unique combinations that sum up to target is less than 150 combinations for the given input.

 

# Example 1:

# Input: candidates = [2,3,6,7], target = 7
# Output: [[2,2,3],[7]]
# Explanation:
# 2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
# 7 is a candidate, and 7 = 7.
# These are the only two combinations.
# Example 2:

# Input: candidates = [2,3,5], target = 8
# Output: [[2,2,2,2],[2,3,3],[3,5]]
# Example 3:

# Input: candidates = [2], target = 1
# Output: []
 

# Constraints:

# 1 <= candidates.length <= 30
# 2 <= candidates[i] <= 40
# All elements of candidates are distinct.
# 1 <= target <= 40

# Time Complexity: O(2^n)
# Space complexity: O(2^n)

# Approach: Backtracking. For every element there will be two choices: whether to include the given element or not
# base case 1: whenever the sum is equal to the target, append the current combination to the result.
# base case 2: when current sum greater than target or current index is greater than or equal to length.
# generate two backtrack calls. One with the current element and one without the current element.

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        length = len(candidates)

        def backtrack(i=0,cmb = []):
            currSum = sum(cmb)
            if currSum == target:
                res.append(cmb)
                return
            elif i>= length or currSum > target:
                return

            cmb.append(candidates[i])
            backtrack(i, cmb[::])
            cmb.pop()
            backtrack(i+1, cmb[::])
                
        backtrack()
        return res    
            