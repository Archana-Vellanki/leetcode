# 75. Sort Colors
# Medium

# Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

# We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

# You must solve this problem without using the library's sort function.


# Example 1:

# Input: nums = [2,0,2,1,1,0]
# Output: [0,0,1,1,2,2]
# Example 2:

# Input: nums = [2,0,1]
# Output: [0,1,2]


# Constraints:

# n == nums.length
# 1 <= n <= 300
# nums[i] is either 0, 1, or 2.


# Follow up: Could you come up with a one-pass algorithm using only constant extra space?


class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # Time complexity: O(2*N) ~ O(N)
        # Space Complexity: O(1)
        length = len(nums)
        count = {0: 0, 1: 0, 2: 0}
        for i in nums:
            count[i] += 1
        for i in range(length):
            if i < count[0]:
                nums[i] = 0
            elif i < count[0] + count[1]:
                nums[i] = 1
            else:
                nums[i] = 2


class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # Time complexity: O(N)
        # Space Complexity: O(1)
        length = len(nums)
        left, right, current = 0, length-1, 0
        while current <= right:
            if nums[current] == 0:
                nums[left], nums[current] = nums[current], nums[left]
                left += 1
                current += 1
            elif nums[current] == 2:
                nums[right], nums[current] = nums[current], nums[right]
                right -= 1
            else:
                current += 1
