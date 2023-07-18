# 55. Jump Game
# Medium
# 16.8K
# 890
# Companies
# You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.

# Return true if you can reach the last index, or false otherwise.


# Example 1:

# Input: nums = [2,3,1,1,4]
# Output: true
# Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
# Example 2:

# Input: nums = [3,2,1,0,4]
# Output: false
# Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.

# Constraints:

# 1 <= nums.length <= 104
# 0 <= nums[i] <= 105

# Time complexity: O(n)
# Space complexity: O(1)

# Approach: 
# Greedy Solution:
# The intuition behind this solution is that it iterates over the array in reverse order, 
# trying to find the earliest index from which we can reach our goal - the last index. 
# We update the goal whenever a new position is found from which we can reach it. 
# Thereby we narrow down the search space and eventually determine if it is possible to reach the last index.

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        length = len(nums)
        goal = length - 1
        for i in range(length - 2, -1, -1):
            if nums[i] + i >= goal:
                goal = i
        return goal == 0