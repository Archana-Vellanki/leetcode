# 53. Maximum Subarray
# Medium

# Given an integer array nums, find the
# subarray
#  with the largest sum, and return its sum.


# Example 1:

# Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6
# Explanation: The subarray [4,-1,2,1] has the largest sum 6.
# Example 2:

# Input: nums = [1]
# Output: 1
# Explanation: The subarray [1] has the largest sum 1.
# Example 3:

# Input: nums = [5,4,-1,7,8]
# Output: 23
# Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.


# Constraints:

# 1 <= nums.length <= 105
# -104 <= nums[i] <= 104


# Follow up: If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.

# -----------------------------------------------------
# Naive Approach: 
Two loops exploring all possible subarrays leading to O(n^2) time complexity

# Divide and Conquer:
# Divide the array into 2 halves until it reaches size 1
# The number of times you can divide until you reach 1 is log₂(n) → This is the depth of the recursion tree.
# At each level of the recursion tree, you calculate:
    # a) Maximum subarray sum in left half 
    # b) Maximum subarray sum in right half 
    # c) Maximum subarray sum such that the subarray crosses the midpoint 
# The maximum sum crossing the midpoint → O(n) time because it requires a single scan of the array to compute sums for the crossing part.
# O(n)×O(logn)=O(nlogn)

# Time complexity: O(nlogn) 
# Space Complexity: O(1)

# Kadane's Algorithm:
# The idea of Kadane’s algorithm is to traverse over the array from left to right and for each element, 
# find the maximum sum among all subarrays ending at that element. The result will be the maximum of all these values. 
# But, the main issue is how to calculate maximum sum among all the subarrays ending at an element in O(1) time?
# To calculate the maximum sum of subarray ending at current element, say maxEnding, we can use the maximum sum ending at the previous element.
# So for any element, we have two choices:

# Choice 1: Extend the maximum sum subarray ending at the previous element by adding the current element to it. 
# If the maximum subarray sum ending at the previous index is positive, then it is always better to extend the subarray.
# Choice 2: Start a new subarray starting from the current element. 
# If the maximum subarray sum ending at the previous index is negative, it is always better to start a new subarray from the current element.

# This means that maxEnding at index i = max(maxEnding at index (i – 1) + arr[i], arr[i]) and the maximum value of maxEnding at any index will be our answer. 

# Time complexity: O(N)
# Space complexity: O(1)

# Approach: This approach maintains a sliding window (with left and right pointers) and iterates through the nums list.
# At every step, discard subarray if the temp sum is negative. (make it zero)
# Update the temp by adding up the current element and update the max_sum as necessary.
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left = 0
        right = 0
        max_sum = nums[left]
        temp = 0
        length = len(nums)
        while right < length:
            if temp < 0:
                temp = 0
                left = right
            temp += nums[right]
            if temp > max_sum:
                max_sum = temp
            right += 1

        return max_sum

# Same approach yet simple
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_sum = nums[0]
        temp_sum = 0
        for i in nums:
            if temp_sum < 0:
                temp_sum = 0
            temp_sum += i
            max_sum = max(max_sum, temp_sum)
        return max_sum

