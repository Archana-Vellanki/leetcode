# 217. Contains Duplicate
# Easy

# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.


# Example 1:

# Input: nums = [1,2,3,1]
# Output: true
# Example 2:

# Input: nums = [1,2,3,4]
# Output: false
# Example 3:

# Input: nums = [1,1,1,3,3,4,3,2,4,2]
# Output: true


# Constraints:

# 1 <= nums.length <= 105
# -109 <= nums[i] <= 109


# Time omplexity: O(nlogn)
# default sort in python is Tim sort: complexity nlogn, then linear time complexity for traversal and comparison hence O(nlogn + n ) ~= O(nlogn)

# Space complexity: O(1)


class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        nums.sort()

        prev = nums[0]

        for i in range(1, len(nums)):
            if nums[i] == prev:
                return True
            prev = nums[i]
        return False

# Time complexity: O(n)- just one traversal

# Space complexity: O(n) worst case the hash set contains all the elements in the list


class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        hashSet = set()
        for i in range(0, len(nums)):
            if nums[i] in hashSet:
                return True
            else:
                hashSet.add(nums[i])
        return False
