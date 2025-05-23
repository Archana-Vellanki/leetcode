# 213. House Robber II
# Solved
# Medium
# Topics
# Companies
# Hint
# You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. Meanwhile, adjacent houses have a security system connected, and it will automatically contact the police if two adjacent houses were broken into on the same night.

# Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

 

# Example 1:

# Input: nums = [2,3,2]
# Output: 3
# Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2), because they are adjacent houses.
# Example 2:

# Input: nums = [1,2,3,1]
# Output: 4
# Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
# Total amount you can rob = 1 + 3 = 4.
# Example 3:

# Input: nums = [1,2,3]
# Output: 3
 

# Constraints:

# 1 <= nums.length <= 100
# 0 <= nums[i] <= 1000

# Time Complexity: O(n)
# Space Complexity: O(1)

# If there’s only one house, just return its money.
# Otherwise, split the circle into two linear cases:
# Case 1: Rob from house 0 to n - 2 (skip the last house)
# Case 2: Rob from house 1 to n - 1 (skip the first house)
# Use a helper function rob_linear(start, end) to solve each case.

class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        l = len(nums)
        if l == 1:
            return nums[0]
        
        def rob_linear(start, end):
            prev, prev2 = nums[start], 0
            maxRob = 0
            for i in range(start+1, end):
                temp = max(prev2 + nums[i], prev)
                prev2 = prev
                prev = temp
            return max(prev, prev2)
          
        rob1 = rob_linear(0, l - 1)
        rob2 = rob_linear(1, l)
      
        return max(rob1, rob2)
