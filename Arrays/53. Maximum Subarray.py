# 53. Maximum Subarray
# Medium

# Given an integer array nums, find the
# subarray
#  with the largest sum, and return its sum.


# Example 1:

# Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6
# Explanation: The subarray [4,-1,2,1] has the largest sum 6.
# Example 2:

# Input: nums = [1]
# Output: 1
# Explanation: The subarray [1] has the largest sum 1.
# Example 3:

# Input: nums = [5,4,-1,7,8]
# Output: 23
# Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.


# Constraints:

# 1 <= nums.length <= 105
# -104 <= nums[i] <= 104


# Follow up: If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.


# Time complexity: O(N) - since only one traversal
# Space complexity: O(1)

# Approach: This approach maintains a sliding window (with left and right pointers) and iterates through the nums list.
# At every step, discard subarray if the temp sum is negative. (make it zero)
# Update the temp by adding up the current element and update the max_sum as necessary.
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left = 0
        right = 0
        max_sum = nums[left]
        temp = 0
        length = len(nums)
        while right < length:
            if temp < 0:
                temp = 0
                left = right
            temp += nums[right]
            if temp > max_sum:
                max_sum = temp
            right += 1

        return max_sum

# Same approach yet simple


class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_sum = nums[0]
        temp_sum = 0
        for i in nums:
            if temp_sum < 0:
                temp_sum = 0
            temp_sum += i
            max_sum = max(max_sum, temp_sum)
        return max_sum
