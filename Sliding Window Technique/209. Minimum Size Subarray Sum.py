# 209. Minimum Size Subarray Sum
# Medium
# 9.6K
# 274
# Companies
# Given an array of positive integers nums and a positive integer target, return the minimal length of a
# subarray
#  whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.


# Example 1:

# Input: target = 7, nums = [2,3,1,2,4,3]
# Output: 2
# Explanation: The subarray [4,3] has the minimal length under the problem constraint.
# Example 2:

# Input: target = 4, nums = [1,4,4]
# Output: 1
# Example 3:

# Input: target = 11, nums = [1,1,1,1,1,1,1,1]
# Output: 0


# Constraints:

# 1 <= target <= 109
# 1 <= nums.length <= 105
# 1 <= nums[i] <= 104


# Follow up: If you have figured out the O(n) solution, try coding another solution of which the time complexity is O(n log(n)).


# Time Complexity: O(n)
# Space Complexity: O(1)
# Approach: Keep increasing the right pointer and adding the elements (at right index) to the sum until as long as the sum is less than target. 
# Once it is greater than target, keep subtracting elements from the left as long as the sum is greater than target.

class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        if max(nums) >= target:
            return 1
        length = len(nums)
        minLen = float('inf')
        windoSum = 0
        left = 0

        for right in range(length):
            windoSum += nums[right]

            while windoSum >= target:
                minLen = min(minLen, right - left + 1)
                windoSum -= nums[left]
                left += 1

        return minLen if minLen != float('inf') else 0
