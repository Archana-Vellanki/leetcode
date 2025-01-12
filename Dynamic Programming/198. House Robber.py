# 198. House Robber
# Solved
# Medium
# Topics
# Companies
# You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

# Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

 

# Example 1:

# Input: nums = [1,2,3,1]
# Output: 4
# Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
# Total amount you can rob = 1 + 3 = 4.
# Example 2:

# Input: nums = [2,7,9,3,1]
# Output: 12
# Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
# Total amount you can rob = 2 + 9 + 1 = 12.
 

# Constraints:

# 1 <= nums.length <= 100
# 0 <= nums[i] <= 400
# Time complexity: O(n)
# Space Complexity: O(n)

# Approach: 
# Start from the last house:
    # If you rob it, you take its value since there’s no house after it.
    # If you skip it, you don’t get any money from that house.
# We use two arrays:
    # dp_incl[i]: Maximum money if house i is robbed.
    # dp_non_incl[i]: Maximum money if house i is skipped.
# Move backward through the houses:
    # At each house, decide whether to rob it or skip it:
        # If you rob it, the total robbed value would be the inclusive sum = current_value + dp_non_incl[i+1](the money you can get by skipping the next house).
        # If you skip it, take the maximum money you could have earned from the next house, whether it was robbed or skipped.
# Return the maximum money possible for house 0 - both inclusive and non_inclusive 

class Solution:
    def rob(self, nums: List[int]) -> int:
        length = len(nums)
        dp_incl = [0]*length
        dp_non_incl = [0]*length
        dp_incl[-1] = nums[-1]
        for i in range(length - 2, -1, -1):
            dp_incl[i] = dp_non_incl[i+1] + nums[i]
            dp_non_incl[i] = max(dp_incl[i+1], dp_non_incl[i+1])
        return max(dp_incl[0], dp_non_incl[0])
