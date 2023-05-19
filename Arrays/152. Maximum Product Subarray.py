# 152. Maximum Product Subarray
# Medium

# Given an integer array nums, find a
# subarray
#  that has the largest product, and return the product.

# The test cases are generated so that the answer will fit in a 32-bit integer.


# Example 1:

# Input: nums = [2,3,-2,4]
# Output: 6
# Explanation: [2,3] has the largest product 6.
# Example 2:

# Input: nums = [-2,0,-1]
# Output: 0
# Explanation: The result cannot be 2, because [-2,-1] is not a subarray.


# Constraints:

# 1 <= nums.length <= 2 * 104
# -10 <= nums[i] <= 10
# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

# Time complexity: O(N)
# Space complexity: O(1)


# Approach: For every iteration, find the minimum and maximum products. Update the res as necessary.
# Edge case when element is zero, the products are intitalised to 1, to compare next elements.
class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = max(nums)  # edge case: when element is zero, the products are intitialised to 1 so that it resumes the comparison with next elements.
        # Ex: (-2,0,-1) here in the second iteration, the element being 0, the products are reinitialized to 1.
        # for the next iteration both max_product and min_product would be -1
        # if res is not max(nums), the result would be -1 because zero is ignored.
        # in order to avoid that res would be intialised to max value.
        max_product = 1
        min_product = 1
        for i in nums:
            if i == 0:
                max_product = 1
                min_product = 1
                continue
            max_product, min_product = max(
                i*max_product, i*min_product, i), min(i*max_product, i*min_product, i)
            res = max(max_product, res)
        return res


# Time complexity: O(N)
# Space complexity: O(1)


# Approach: At each iteration, when element is negative, we swap the max_product and min_product variables before updating them.
# This ensures that the max_product always represents the maximum product of a subarray, and the min_product represents the minimum product of a subarray.
# This swap takes care of the cases where min_product is negative, and the negative element can create a new maximum product.
class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = max_product = min_product = nums[0]

        for i in nums[1:]:
            if i < 0:
                # Swap max_product and min_product
                max_product, min_product = min_product, max_product

            max_product = max(i, max_product * i)  # Update max_product
            min_product = min(i, min_product * i)  # Update min_product

            res = max(res, max_product)  # Update res with the maximum product

        return res
