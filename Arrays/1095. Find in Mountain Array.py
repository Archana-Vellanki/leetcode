# 1095. Find in Mountain Array
# Hard

# (This problem is an interactive problem.)

# You may recall that an array arr is a mountain array if and only if:

# arr.length >= 3
# There exists some i with 0 < i < arr.length - 1 such that:
# arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
# arr[i] > arr[i + 1] > ... > arr[arr.length - 1]
# Given a mountain array mountainArr, return the minimum index such that mountainArr.get(index) == target. If such an index does not exist, return -1.

# You cannot access the mountain array directly. You may only access the array using a MountainArray interface:

# MountainArray.get(k) returns the element of the array at index k (0-indexed).
# MountainArray.length() returns the length of the array.
# Submissions making more than 100 calls to MountainArray.get will be judged Wrong Answer. Also, any solutions that attempt to circumvent the judge will result in disqualification.


# Example 1:

# Input: array = [1,2,3,4,5,3,1], target = 3
# Output: 2
# Explanation: 3 exists in the array, at index=2 and index=5. Return the minimum index, which is 2.
# Example 2:

# Input: array = [0,1,2,4,2,1], target = 3
# Output: -1
# Explanation: 3 does not exist in the array, so we return -1.


# Constraints:

# 3 <= mountain_arr.length() <= 104
# 0 <= target <= 109
# 0 <= mountain_arr.get(index) <= 109


# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
# class MountainArray(object):
#    def get(self, index):
#        """
#        :type index: int
#        :rtype int
#        """
#
#    def length(self):
#        """
#        :rtype int
#        """

class Solution(object):
    def peakIndexInMountainArray(self, mountain_arr, length):
        left = 0
        right = length - 1

        while left < right - 1:
            mid = (left+right)//2
            mid_element = mountain_arr.get(mid)
            pre_mid = mountain_arr.get(mid - 1)

            if pre_mid < mid_element:
                left = mid
            else:
                right = mid

        return left

    def binarySearch(self, left, right, target, mountain_arr, isDesc):
        """
        Time Complexity: O(logN)
        Space Complexity: O(1)
        isDesc denotes if the array is ascending or descending
        """
        while left < right:
            mid = (left + right)//2
            mid_element = mountain_arr.get(mid)
            if mid_element == target:
                return mid
            elif mid_element < target:
                if isDesc:
                    right = mid
                else:
                    left = mid + 1
            else:
                if isDesc:
                    left = mid + 1
                else:
                    right = mid
        if mountain_arr.get(left) == target:
            return left
        else:
            return -1

    def findInMountainArray(self, target, mountain_arr):
        """
        :type target: integer
        :type mountain_arr: MountainArray
        :rtype: integer
        """
        length = mountain_arr.length()

        # find Peak position
        peak = self.peakIndexInMountainArray(mountain_arr, length)
        peak_element = mountain_arr.get(peak)

        # check if the target is out of bounds or if it is the peak
        if target > peak_element:
            return -1
        elif target < mountain_arr.get(0) and target < mountain_arr.get(length - 1):
            return -1
        elif peak_element == target:
            return peak

        # search in the ascending part
        index = self.binarySearch(0, peak, target, mountain_arr, False)
        if index != -1:
            return index
        else:
            # the target is not present in the ascending part hence it is searched for in the descending part i.e., after the peak
            return self.binarySearch(peak, length - 1, target, mountain_arr, True)
