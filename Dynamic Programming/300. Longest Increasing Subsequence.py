# 300. Longest Increasing Subsequence
# Solved
# Medium
# Topics
# Companies
# Given an integer array nums, return the length of the longest strictly increasing
# subsequence
# .


# Example 1:

# Input: nums = [10,9,2,5,3,7,101,18]
# Output: 4
# Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.
# Example 2:

# Input: nums = [0,1,0,3,2,3]
# Output: 4
# Example 3:

# Input: nums = [7,7,7,7,7,7,7]
# Output: 1


# Constraints:

# 1 <= nums.length <= 2500
# -104 <= nums[i] <= 104


# Follow up: Can you come up with an algorithm that runs in O(n log(n)) time complexity?


# Approach: followed the neetcode video, coming from the last index,
# since the last index doesnt have any other element after it to include in the subsequence,
# the longest increasing subsequence(LIS) at last index would be of length 1
# Similarly for the last but one index, if nums[last - 1] < nums[last], then we can include the current element in the LIS, else it would be 1.
# We can continue doing this till the first element and return the max length at the end
# Time complexity: O(n^2)
# Space complexity: O(n)
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)

        if n == 1:
            return n

        LIS = [1] * n
        # longest = 1
        for i in range(n-2, -1, -1):
            # print(LIS.items())
            # longest_at_i = 1
            for j in range(i+1, n):
                if nums[i] < nums[j]:
                    LIS[i] = max(LIS[i], 1 + LIS[j])
            # longest = max(longest, LIS[i])
        return max(LIS)
