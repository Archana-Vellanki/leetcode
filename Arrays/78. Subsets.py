# 78. Subsets
# Medium
# Given an integer array nums of unique elements, return all possible
# subsets
#  (the power set).

# The solution set must not contain duplicate subsets. Return the solution in any order.


# Example 1:

# Input: nums = [1,2,3]
# Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
# Example 2:

# Input: nums = [0]
# Output: [[],[0]]


# Constraints:

# 1 <= nums.length <= 10
# -10 <= nums[i] <= 10
# All the numbers of nums are unique.


# for the base case, let the nums contains just a single element:
# nums = [3]
# the powerSet would be [[], [3]]
# if nums = [2,3]
# then powerSet = [[], [3], [2], [2,3]]
# which is obtained by keeping all the elements as is and when each element in the powerSet is appended with the element 2


# Backtracking approach:
# The function checks if the nums array is empty. If it is, the function returns the powerSet as it is, containing only the empty subset.

# If the nums array is not empty, the function eliminates the first element and recursively calls itself with the remaining elements of the nums array and the powerSet.

# Finally, for each subset in the powerSet, the function generates a new subset by adding the first element of the nums array to it.

# The function returns the powerSet which contains all possible subsets of the input array nums.

# Time Complexity: O(2^N) since each element in nums can either be included or excluded from a given subset, giving 2 options for each element.
# Space Complexity: O(2^N) since we have to store all the subsets

class Solution(object):
    def subsets(self, nums, powerSet=None):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # To avoid mutable default value, initiate powerSet value to None and change it when required.
        if powerSet is None:
            powerSet = [[]]

        # In the base case where nums is an empty array, return [[]]
        if nums == []:
            return powerSet

        # If the nums array is not empty, the function eliminates the first element
        # and recursively calls itself with the remaining elements of the nums array and the powerSet.
        powerSet = self.subsets(nums[1:], powerSet)

        # for each subset in the powerSet, the function generates a new subset by adding the first element of the nums array to it.
        # The new subset is then appended to the powerSet.
        num = nums[0]
        pow_len = len(powerSet)
        for i in range(pow_len):
            powerSet.append(powerSet[i] + [num])
        return powerSet
