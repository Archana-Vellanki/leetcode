# 268. Missing Number
# Easy

# Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.

 

# Example 1:

# Input: nums = [3,0,1]
# Output: 2
# Explanation: n = 3 since there are 3 numbers, so all numbers are in the range [0,3]. 2 is the missing number in the range since it does not appear in nums.
# Example 2:

# Input: nums = [0,1]
# Output: 2
# Explanation: n = 2 since there are 2 numbers, so all numbers are in the range [0,2]. 2 is the missing number in the range since it does not appear in nums.
# Example 3:

# Input: nums = [9,6,4,2,3,5,7,0,1]
# Output: 8
# Explanation: n = 9 since there are 9 numbers, so all numbers are in the range [0,9]. 8 is the missing number in the range since it does not appear in nums.
 

# Constraints:

# n == nums.length
# 1 <= n <= 104
# 0 <= nums[i] <= n
# All the numbers of nums are unique.
 

# Follow up: Could you implement a solution using only O(1) extra space complexity and O(n) runtime complexity?

# Time complexity: O(n)
# Space complexity: O(1)

# Approach: Bit manipulation- xor of same numbers is 0. 
# xor all numbers in range[0,n] then xor all numbers in nums. 
# all numbers except the missing number would be xor'd twice and hence the xor value will be the value which is in range[0,n] but missing in nums
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        xor = 0
        for i in range(n+1):
            xor ^= i
        for i in nums:
            xor ^= i
        return xor

# Time complexity: O(n)
# Space complexity: O(1)

# Approach: sum of n numbers  = [n*(n+1)]/2
# iterate over nums and subtract each element from the sum. The missing number would be left out
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        return (n*(n+1))//2 - sum(nums)