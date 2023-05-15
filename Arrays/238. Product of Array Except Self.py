# 238. Product of Array Except Self
# Medium

# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

# You must write an algorithm that runs in O(n) time and without using the division operation.


# Example 1:

# Input: nums = [1,2,3,4]
# Output: [24,12,8,6]
# Example 2:

# Input: nums = [-1,1,0,-3,3]
# Output: [0,0,9,0,0]


# Constraints:

# 2 <= nums.length <= 105
# -30 <= nums[i] <= 30
# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.


# Follow up: Can you solve the problem in O(1) extra space complexity? (The output array does not count as extra space for space complexity analysis.)

# Time complexity: O(n)
# two linear traversals

# Space complexity: O(n)
# two arrays to store the prefix and suffix products

class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        length = len(nums)
        prefixProduct = [1 for i in range(length)]
        suffixProduct = [1 for i in range(length)]

        # prefix product
        # example: [1,2,3,4]
        # [1,1,2,6]
        for i in range(1, length):
            prefixProduct[i] = prefixProduct[i-1] * nums[i-1]

        # suffix product
        # [24,12,4,1]
        for i in range(length - 2, -1, -1):
            suffixProduct[i] = suffixProduct[i+1] * nums[i+1]

        # final ans by multiplying the corresponding elements of prefixProduct and suffixProduct
        return [prefixProduct[i]*suffixProduct[i] for i in range(length)]


# Time complexity: O(n)
# two linear traversals

# Space complexity: O(1)
# The output array does not count as extra space for space complexity analysis.
class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        length = len(nums)
        output = [1 for i in range(length)]

        # left product
        for i in range(1, length):
            output[i] = output[i-1] * nums[i-1]

        rightProduct = 1
        # simultaneously store the rightProduct and update the output
        # output is the product of the calculated right product(suffix product) and the left product(which is already calculated in the previous loop)
        for i in range(length - 1, -1, -1):
            output[i] = rightProduct * output[i]
            rightProduct *= nums[i]
        return output
