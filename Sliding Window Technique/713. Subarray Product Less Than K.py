# 713. Subarray Product Less Than K
# Solved
# Medium
# Topics
# Companies
# Hint
# Given an array of integers nums and an integer k, return the number of contiguous subarrays where the product of all the elements in the subarray is strictly less than k.


# Example 1:

# Input: nums = [10,5,2,6], k = 100
# Output: 8
# Explanation: The 8 subarrays that have product less than 100 are:
# [10], [5], [2], [6], [10, 5], [5, 2], [2, 6], [5, 2, 6]
# Note that [10, 5, 2] is not included as the product of 100 is not strictly less than k.
# Example 2:

# Input: nums = [1,2,3], k = 0
# Output: 0


# Constraints:

# 1 <= nums.length <= 3 * 104
# 1 <= nums[i] <= 1000
# 0 <= k <= 106

# Approach: Sliding window technique. keep moving the end pointer and updating the product.
# While the product is greater than k, keep moving the start pointer forward and
# updating the product by 'product /= nums[start]', with this you are removing the element at start index.
# At each step, calculate the number of subarrays using the start and end indices itself 'result += end - start + 1'.
# Input: nums = [10, 5, 2, 6], k = 100

# ======== (End for loop, r = 0 snapshot) =============
# [10, 5, 2, 6]
#   r
#   l
# prod = 10
# cnt += 1


# ======== (End for loop, r = 1 snapshot) =============
# [10, 5, 2, 6]
#      r
#   l
# prod = 50
# cnt += 2


# ======== (r = 2, prod >= k snapshot) ================
# [10, 5, 2, 6]
#         r
#   l
# prod = 100, >= k,
# keep moving l till < k


# ======== (End for loop, r = 2 snapshot) =============
# [10, 5, 2, 6]
#         r
#      l
# prod = 10
# cnt += 2


# ======== (End for loop, r = 3 snapshot) =============
# [10, 5, 2, 6]
#            r
#      l
# prod = 60
# cnt += 3
class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        result = 0
        start = 0
        end = 0
        product = 1
        length = len(nums)
        if k == 0:
            return 0
        while end < length:
            product *= nums[end]
            while product >= k and start <= end:
                product /= nums[start]
                start += 1
            result += end - start + 1
            end += 1
        return result
