# 33. Search in Rotated Sorted Array
# Medium

# There is an integer array nums sorted in ascending order (with distinct values).

# Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

# Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

# You must write an algorithm with O(log n) runtime complexity.


# Example 1:

# Input: nums = [4,5,6,7,0,1,2], target = 0
# Output: 4
# Example 2:

# Input: nums = [4,5,6,7,0,1,2], target = 3
# Output: -1
# Example 3:

# Input: nums = [1], target = 0
# Output: -1


# Constraints:

# 1 <= nums.length <= 5000
# -104 <= nums[i] <= 104
# All values of nums are unique.
# nums is an ascending array that is possibly rotated.
# -104 <= target <= 104


# Time complexity: O(logN)
# Space complexity: O(1)

# Approach: Find the position of the minimum element in the rotated sorted array.
# check if the element is between the 0 index and index of minimum element or in between the index of minimum element and the last element
# perform binary search accordingly
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        mini = self.pivot(nums)
        if target < nums[mini]:
            return -1
        elif target == nums[mini]:
            return mini
        else:
            left = 0 if target >= nums[0] else mini
            right = len(nums) - 1 if target <= nums[-1] else mini
            while left <= right:
                mid = (left + right)//2
                if target < nums[mid]:
                    right = mid - 1
                elif target > nums[mid]:
                    left = mid + 1
                else:
                    return mid
            return -1

    def pivot(self, nums):
        left = 0
        right = len(nums) - 1

        while left < right:
            mid = (left + right)//2
            if nums[left] < nums[right]:
                return left
            else:
                if nums[mid] > nums[right]:
                    left = mid + 1
                else:
                    right = mid
        return left

# same time complexity and space complexity but different implementation by finding the largest element and then doing th binary search


class Solution(object):
    def findLargest(self, nums):
        l = 0
        r = len(nums) - 1  # 7
        if nums[l] < nums[r]:
            return r
        print(nums)
        while l < r:
            mid = (l + r)//2
            # print(l, mid, r)
            if nums[l] < nums[r]:
                return r
            else:
                if nums[l] < nums[mid]:
                    l = mid
                else:
                    r = mid
        return l

    def binarySearch(self, left, right, nums, target):
        print(left, right, nums, target)
        while left < right:
            mid = (left + right)//2
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid
            else:
                return mid
        return left if nums[left] == target else -1

    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        pivot = self.findLargest(nums)

        result = self.binarySearch(0, pivot, nums, target)

        if result != -1:
            return result
        else:
            length = len(nums)
            if pivot < length - 1:
                return self.binarySearch(pivot + 1, length - 1, nums, target)
            else:
                return pivot if nums[pivot] == target else - 1


# class Solution(object):
#     def find_pivot(self, nums):
#         length = len(nums)
#         l = 0
#         r = length - 1

#         if nums[l] < nums[r]:
#             return -1

#         while l < r:
#             mid = (l+r)//2
#             if nums[mid] > nums[mid+1]:
#                 return mid
#             else:
#                 if nums[0] < nums[mid]:
#                     l = mid
#                 else:
#                     r = mid
#         return r

#     def binarySearch(self, left, right, nums, target):
#         while left <= right:
#             mid = (left + right)//2
#             if nums[mid] == target:
#                 return mid
#             elif nums[mid] < target:
#                 left = mid + 1
#             else:
#                 right = mid - 1
#         return -1

#     def search(self, nums, target):
#         """
#         :type nums: List[int]
#         :type target: int
#         :rtype: int
#         """
#         length = len(nums)

#         pivot = self.find_pivot(nums)

#         if pivot == -1:
#             return self.binarySearch(0, length - 1, nums, target)
#         if target > nums[pivot]:
#             return -1
#         if target == nums[pivot]:
#             return pivot

#         if target >= nums[0]:
#             return self.binarySearch(0, pivot, nums, target)
#         else:
#             return self.binarySearch(pivot+1, length - 1,  nums, target)
