# 350. Intersection of Two Arrays II
# Easy

# Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must appear as many times as it shows in both arrays and
# you may return the result in any order.


# Example 1:

# Input: nums1 = [1, 2, 2, 1], nums2 = [2, 2]
# Output: [2, 2]
# Example 2:

# Input: nums1 = [4, 9, 5], nums2 = [9, 4, 9, 8, 4]
# Output: [4, 9]
# Explanation: [9, 4] is also accepted.


# Constraints:

# 1 <= nums1.length, nums2.length <= 1000
# 0 <= nums1[i], nums2[i] <= 1000


# Follow up:

# What if the given array is already sorted? How would you optimize your algorithm?
# What if nums1's size is small compared to nums2's size? Which algorithm is better?
# What if elements of nums2 are stored on disk, and the memory is limited such that you cannot load all elements into the memory at once?


class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        # Time complexity = O(m+n)
        # Space complexity = O(m)
        len1, len2 = len(nums1), len(nums2)
        ans = []
        hash1 = {}

        for i in range(len1):
            # can use get method with default value to be returned if the key is not found
            if nums1[i] in hash1:
                hash1[nums1[i]] += 1
            else:
                hash1[nums1[i]] = 1

        for i in range(len2):
            if nums2[i] in hash1:
                ans.append(nums2[i])
                if hash1[nums2[i]] == 1:
                    hash1.pop(nums2[i])
                else:
                    hash1[nums2[i]] -= 1
        return ans


# Solution 2: Sorting
    # Time complexity: O(max(m,n) log max(m,n)) because of the sorting
    # Space complexity: O(1)
# Another way to solve this problem is to sort both arrays and then use two pointers to iterate through them.
# If the elements at the two pointers are equal, add the element to the result array and increment both pointers.
# Otherwise, increment the pointer of the array with the smaller element.
class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        len1, len2 = len(nums1), len(nums2)
        ans = []
        i, j = 0, 0
        nums1.sort()
        nums2.sort()
        while i < len1 and j < len2:
            if nums1[i] == nums2[j]:
                ans.append(nums1[i])
                i += 1
                j += 1
            elif nums1[i] < nums2[j]:
                i += 1
            else:
                j += 1
        return ans
