# 45. Jump Game II
# Solved
# Medium
# Topics
# premium lock icon
# Companies
# You are given a 0-indexed array of integers nums of length n. You are initially positioned at nums[0].

# Each element nums[i] represents the maximum length of a forward jump from index i. In other words, if you are at nums[i], you can jump to any nums[i + j] where:

# 0 <= j <= nums[i] and
# i + j < n
# Return the minimum number of jumps to reach nums[n - 1]. The test cases are generated such that you can reach nums[n - 1].

 

# Example 1:

# Input: nums = [2,3,1,1,4]
# Output: 2
# Explanation: The minimum number of jumps to reach the last index is 2. Jump 1 step from index 0 to 1, then 3 steps to the last index.
# Example 2:

# Input: nums = [2,3,0,1,4]
# Output: 2
 

# Constraints:

# 1 <= nums.length <= 104
# 0 <= nums[i] <= 1000
# It's guaranteed that you can reach nums[n - 1].

# Approach:
# farthest keeps track of the farthest point we can reach with the current set of jumps.
# current_end marks the boundary of the current jump.
# When i == current_end, it means we’ve used a jump and now need to jump again to proceed, so we:
# Increment jumps
# Update current_end = farthest

class Solution:
    def jump(self, nums: List[int]) -> int:
        '''
        0 1 2 3 4 
        2 3 0 1 4 

        i       farthest         current_end    jumps
        0       0                      0          0
        0       max(0, 0+2) = 2        2          1
        1       max(2, 1+3) = 4        2          1
        2       max(4, 2+0) = 4        4          2
        3       max(4, 3+1) = 4        4          2

        '''
        jumps = 0
        farthest = 0
        current_end = 0
        for i in range(len(nums) - 1):
            farthest = max(farthest, i + nums[i])
            if i == current_end:
                jumps += 1
                current_end = farthest
        return jumps
