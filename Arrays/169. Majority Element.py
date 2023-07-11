# 169. Majority Element
# Easy
# 15.6K
# 456
# Companies
# Given an array nums of size n, return the majority element.

# The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.


# Example 1:

# Input: nums = [3,2,3]
# Output: 3
# Example 2:

# Input: nums = [2,2,1,1,1,2,2]
# Output: 2


# Constraints:

# n == nums.length
# 1 <= n <= 5 * 104
# -109 <= nums[i] <= 109


# Follow-up: Could you solve the problem in linear time and in O(1) space?

# Time complexity: O(n)
# Space complexity: O(1)
# Approach:
# The intuition behind the Moore's Voting Algorithm is based on the fact that if there is a majority element in an array,
# it will always remain in the lead, even after encountering other elements.

# Implementation:
# Initialize two variables: count and candidate. Set count to 0 and candidate to an arbitrary value.
# Iterate through the array nums:
# a. If count is 0, assign the current element as the new candidate and increment count by 1.
# b. If the current element is the same as the candidate, increment count by 1.
# c. If the current element is different from the candidate, decrement count by 1.
# After the iteration, the candidate variable will hold the majority element.


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        candidate = nums[0]

        for each in nums:
            if each == candidate:
                count += 1
            else:
                count -= 1
            if count == 0:
                candidate = each
                count += 1
        return candidate


# Time complexity: O(nlogn)
# Space complexity: O(1)
# Approach: Sorting, if majority element is present in the array it will definitely be in the middle position of the array since its count is greater than n/2 times

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        length = len(nums)

        nums.sort()
        return nums[length//2]


# Time complexity: O(n)
# Space complexity: O(n)
# Approach: counting Hashmap

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        length = len(nums)
        counts = {}
        major = None

        for each in nums:
            counts[each] = counts.get(each, 0) + 1
            if counts[each] > length//2:
                major = each
        return major
