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

"""
Time complexity: O(logN)
Space complexity: O(1)

"Intuition: Even though the array is rotated, one half is always sorted. By determining which half is sorted, you can quickly decide whether the target lies within that half, and then continue narrowing down your search accordingly. 

Approach: Dividing the Array:
Compare mid element with the right most element to determine if the right half is sorted. 

1. If nums[mid] <= nums[left] the right part is in order; 
      Check if the target lies between nums[mid] and nums[right]. If it does, narrow your search to the right half; if not, search the left half.

2. otherwise, the left part must be sorted.
      Check if the target lies between nums[left] and nums[mid]. If it does, you know the target must be in this sorted part, so you move your search to the left. Otherwise, you search the right half."
"""
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        length = len(nums)
        if length == 1:
            return 0 if nums[0]==target else -1

        lo, hi = 0, length - 1
        while lo < hi:
            mid = (lo + hi)//2
            if nums[mid] == target:
                return mid
            if nums[mid] < nums[hi]:
                # Mid to hi is sorted. 
                if target > nums[mid] and target <= nums[hi]:
                    # target is between mid and hi
                    lo = mid + 1
                else:
                    hi = mid
            else:
                # Lo to mid is sorted
                if target >= nums[lo] and target < nums[mid]:
                    # target is between lo and mid
                    hi = mid - 1
                else:
                    lo = mid + 1
        return lo if nums[lo]== target else -1
