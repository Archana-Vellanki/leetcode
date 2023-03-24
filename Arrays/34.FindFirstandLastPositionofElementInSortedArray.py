# 34. Find First and Last Position of Element in Sorted Array
# Medium

# Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

# If target is not found in the array, return [-1, -1].

# You must write an algorithm with O(log n) runtime complexity.


# Example 1:

# Input: nums = [5,7,7,8,8,10], target = 8
# Output: [3,4]
# Example 2:

# Input: nums = [5,7,7,8,8,10], target = 6
# Output: [-1,-1]
# Example 3:

# Input: nums = [], target = 0
# Output: [-1,-1]


# Constraints:

# 0 <= nums.length <= 105
# -109 <= nums[i] <= 109
# nums is a non-decreasing array.
# -109 <= target <= 109

class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        length = len(nums)

        l = 0
        r = length - 1

        while l <= r:
            mid = (l + r)//2
            if nums[mid] < target:
                l = mid+1
            elif nums[mid] > target:
                r = mid - 1
            else:
                if nums[l] == target and nums[r] == target:
                    return [l, r]
                elif nums[l] == target:
                    r = r - 1
                elif nums[r] == target:
                    l = l + 1
                else:
                    l = l + 1
                    r = r - 1
        return [-1, -1]
