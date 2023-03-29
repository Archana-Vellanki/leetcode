# 852. Peak Index in a Mountain Array
# Medium

# An array arr a mountain if the following properties hold:

# arr.length >= 3
# There exists some i with 0 < i < arr.length - 1 such that:
# arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
# arr[i] > arr[i + 1] > ... > arr[arr.length - 1]
# Given a mountain array arr, return the index i such that arr[0] < arr[1] < ... < arr[i - 1] < arr[i] > arr[i + 1] > ... > arr[arr.length - 1].

# You must solve it in O(log(arr.length)) time complexity.


# Example 1:

# Input: arr = [0,1,0]
# Output: 1
# Example 2:

# Input: arr = [0,2,1,0]
# Output: 1
# Example 3:

# Input: arr = [0,10,5,2]
# Output: 1


# Constraints:

# 3 <= arr.length <= 105
# 0 <= arr[i] <= 106
# arr is guaranteed to be a mountain array.


""" 
1. Mountain array is also known as "bitonic array": A Bitonic array is an array of numbers which is first strictly increasing then after a point strictly decreasing.

2. For infinite array, use binary search by doubling the searching window every time to get logarithmic complexity.

3. order agnostic binary search - one modification from the binary search to check the order of the sorting i.e, ascending or descending.
"""


class Solution(object):
    def peakIndexInMountainArray(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        # Time complexity: O(logN)
        # Space complexity: O(1)

        length = len(arr)
        l = 0
        r = length - 1

        while l < r - 1:
            mid = (l+r)//2
            if arr[mid - 1] < arr[mid]:
                l = mid
            else:
                r = mid
        return l
