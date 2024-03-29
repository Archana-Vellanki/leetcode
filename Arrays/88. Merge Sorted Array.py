# 88. Merge Sorted Array
# Easy

# You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

# Merge nums1 and nums2 into a single array sorted in non-decreasing order.

# The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.


# Example 1:

# Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
# Output: [1,2,2,3,5,6]
# Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
# The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.
# Example 2:

# Input: nums1 = [1], m = 1, nums2 = [], n = 0
# Output: [1]
# Explanation: The arrays we are merging are [1] and [].
# The result of the merge is [1].
# Example 3:

# Input: nums1 = [0], m = 0, nums2 = [1], n = 1
# Output: [1]
# Explanation: The arrays we are merging are [] and [1].
# The result of the merge is [1].
# Note that because m = 0, there are no elements in nums1. The 0 is only there to ensure the merge result can fit in nums1.


# Constraints:

# nums1.length == m + n
# nums2.length == n
# 0 <= m, n <= 200
# 1 <= m + n <= 200
# -109 <= nums1[i], nums2[j] <= 109

class Solution(object):
    # Time complexity: O(m*n)
    # space complexity: O(1)
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        i, j = 0, 0
        # merging it in place;
        # if the element at index i in nums1 > element at index j in nums2,
        # move the elements in nums1 by 1 position and insert the nums2 element and increase both j and m since the elements have been moved to next index
        # else, it means the element is in right position so we can just increase i by 1 and proceed further
        while i < m and j < n:
            if nums1[i] > nums2[j]:
                nums1[i+1:] = nums1[i:-1]
                nums1[i] = nums2[j]
                j += 1
                m += 1
            else:
                i += 1
        if j < n:
            nums1[i:] = nums2[j:]

# better approach


class Solution(object):
    # Time complexity: O(m+n)
    # space complexity: O(1)
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        # Initialize pointers for nums1, nums2, and the merged array
        i = m - 1
        j = n - 1
        k = m + n - 1

        # Merge nums1 and nums2 from the back
        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1

        # Exits only when either of i or j is less than zero
        # if nums1 has left out elements(i > 0 and j < 0): all the elements are less than those of nums2 and hence are in place
        # if nums2 has left out elements (j > 0 and i < 0): all the nums1 initial elements are to be replaced with the elements in nums2.
        # Hence Append any remaining elements from nums2 to nums1.
        nums1[:j+1] = nums2[:j+1]
