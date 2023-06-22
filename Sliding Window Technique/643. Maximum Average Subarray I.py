# 643. Maximum Average Subarray I
# Easy

# You are given an integer array nums consisting of n elements, and an integer k.

# Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value.
# Any answer with a calculation error less than 10-5 will be accepted.


# Example 1:

# Input: nums = [1,12,-5,-6,50,3], k = 4
# Output: 12.75000
# Explanation: Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75
# Example 2:

# Input: nums = [5], k = 1
# Output: 5.00000


# Constraints:

# n == nums.length
# 1 <= k <= n <= 105
# -104 <= nums[i] <= 104


# Time Complexity: O(n)
# Space complexity: O(1)
# Approach: Maintain a window(subarray) of size k. At each iteration, eliminate the left element and add the right element to maintain the size of the subarray as k.
# Compute the sum of each subarray and update the maximum sum. (since k is constant, maximum sum gives the maximum avg. Instead of calculating the average everytime just keep track of the sum)
# Return the sum divided by k post converting it to float.

class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """

        currSum = sum(nums[0:k])
        left = 0
        right = k
        length = len(nums)
        maxSum = currSum
        while right < length:
            currSum = currSum - nums[left] + nums[right]
            maxSum = max(maxSum, currSum)
            left += 1
            right += 1

        return float(maxSum)/k
