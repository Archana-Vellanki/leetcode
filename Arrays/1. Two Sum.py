# 1. Two Sum


# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.


# Example 1:

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
# Example 2:

# Input: nums = [3,2,4], target = 6
# Output: [1,2]
# Example 3:

# Input: nums = [3,3], target = 6
# Output: [0,1]


# Constraints:

# 2 <= nums.length <= 104
# -109 <= nums[i] <= 109
# -109 <= target <= 109
# Only one valid answer exists.


# Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?

# Brute force approach: O(n^2) - add each element with every other element in the array and check if the sum is equal to the target

# Space complexity: O(n)
# Time complexity: O(n)
# Approach: Use a hashmap to store every element that we came across and its index.
# Also before adding an element to the hashmap, check if the difference between the target and the current element is already there in it. If it is then return the element.
def twoSum(self, nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    hashmap = {}
    for i in range(len(nums)):
        diff = target - nums[i]
        if diff in hashmap:
            return([i, hashmap[diff]])
        hashmap[nums[i]] = i
