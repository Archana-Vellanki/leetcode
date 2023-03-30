# 81. Search in Rotated Sorted Array II
# Medium

# There is an integer array nums sorted in non-decreasing order (not necessarily with distinct values).

# Before being passed to your function, nums is rotated at an unknown pivot index k (0 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,4,4,5,6,6,7] might be rotated at pivot index 5 and become [4,5,6,6,7,0,1,2,4,4].

# Given the array nums after the rotation and an integer target, return true if target is in nums, or false if it is not in nums.

# You must decrease the overall operation steps as much as possible.


# Example 1:

# Input: nums = [2,5,6,0,0,1,2], target = 0
# Output: true
# Example 2:

# Input: nums = [2,5,6,0,0,1,2], target = 3
# Output: false


# Constraints:

# 1 <= nums.length <= 5000
# -104 <= nums[i] <= 104
# nums is guaranteed to be rotated at some pivot.
# -104 <= target <= 104


# Follow up: This problem is similar to Search in Rotated Sorted Array, but nums may contain duplicates. Would this affect the runtime complexity? How and why?

class Solution(object):
    def findPivot(self, nums):
        length = len(nums)
        l = 0
        r = length - 1
        if nums[l] < nums[r]:
            return -1
        while l < r:
            mid = (l + r)//2
            if mid < length - 1 and nums[mid] > nums[mid+1]:
                return mid
            elif nums[l] > nums[mid]:
                r = mid
            elif nums[l] < nums[mid]:
                l = mid
            else:
                if nums[l] > nums[l + 1]:
                    return l
                if nums[l] == nums[r]:
                    # start, end and mid are equal
                    l += 1
                    r -= 1
                elif nums[l] == nums[mid]:
                    # only start and mid are equal
                    l += 1
                elif nums[r] == nums[mid]:
                    # only end and mid are equal
                    r -= 1
        return l

    def binarySearch(self, left, right, nums, target):
        # print(target, nums[left:right])
        while left <= right:
            mid = (left + right)//2
            if target == nums[mid]:
                # print("true")
                return True
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return False

    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        pivot = self.findPivot(nums)
        print(pivot)
        length = len(nums)

        if pivot == -1:
            return self.binarySearch(0, length - 1, nums, target)
        elif target > nums[pivot]:
            return False
        elif target >= nums[0]:
            print("target >= nums[0]")
            return self.binarySearch(0, pivot, nums, target)
        else:
            print("target < nums[0]")
            return self.binarySearch(pivot+1, length - 1, nums, target)
