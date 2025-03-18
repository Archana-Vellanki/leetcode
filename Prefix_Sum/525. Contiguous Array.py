# 525. Contiguous Array
# Solved
# Medium
# Topics
# Companies
# Given a binary array nums, return the maximum length of a contiguous subarray with an equal number of 0 and 1.

 

# Example 1:

# Input: nums = [0,1]
# Output: 2
# Explanation: [0, 1] is the longest contiguous subarray with an equal number of 0 and 1.
# Example 2:

# Input: nums = [0,1,0]
# Output: 2
# Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.
# Example 3:

# Input: nums = [0,1,1,1,1,1,0,0,0]
# Output: 6
# Explanation: [1,1,1,0,0,0] is the longest contiguous subarray with equal number of 0 and 1.
 

# Constraints:

# 1 <= nums.length <= 105
# nums[i] is either 0 or 1.

# Approach: Key Idea: If the difference between the counts of 1's and 0's is same at two indices, the subarray between those two indices must be having equal number of 0s and 1s.
# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        # count_diff = []
        hashmap = {}
        zero_count = 0
        one_count = 0
        max_length = 0
        for i in range(len(nums)):
            # print(hashmap, max)
            if nums[i] == 0:
                zero_count += 1
            else:
                one_count += 1
            diff = one_count - zero_count
            if diff == 0:
                max_length = max(max_length, i+1)
            if diff in hashmap:
                max_length = max(max_length, i - hashmap[diff])
            else:
                hashmap[diff] = i
        return max_length
            
        
