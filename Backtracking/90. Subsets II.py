# 90. Subsets II
# Medium

# Given an integer array nums that may contain duplicates, return all possible 
# subsets
#  (the power set).

# The solution set must not contain duplicate subsets. Return the solution in any order.


# Example 1:

# Input: nums = [1,2,2]
# Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]
# Example 2:

# Input: nums = [0]
# Output: [[],[0]]
 

# Constraints:

# 1 <= nums.length <= 10
# -10 <= nums[i] <= 10


# Time complexity: O(n.2^n)
# Space complexity: O(n.2^n)
# Approach: backtracking
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        
        def backtrack(i=0, subset=[]):
            # base case
            if i == len(nums):
                res.append(subset[:])
                return
            # Subsets with the current element
            subset.append(nums[i])
            backtrack(i + 1, subset)

            # Subsets without the current element
            subset.pop()
            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1
            backtrack(i + 1, subset)
        
        backtrack()
        return res