# 560. Subarray Sum Equals K
# Solved
# Medium
# Topics
# Companies
# Hint
# Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.

# A subarray is a contiguous non-empty sequence of elements within an array.

 

# Example 1:

# Input: nums = [1,1,1], k = 2
# Output: 2
# Example 2:

# Input: nums = [1,2,3], k = 3
# Output: 2
 

# Constraints:

# 1 <= nums.length <= 2 * 104
# -1000 <= nums[i] <= 1000
# -107 <= k <= 107

# Approach:
# Example:
#     [_, _, _, _, _, _], k = 5
#      _  _|            ==> prefixSum = 3
#      _  _  _  _  _|   ==> prefixSum = 8
#           |_  _  _|   ==> required subarray with sum = 5
# With a combination of Hashmap and prefixSum you can find out the sum of all possible subarrays 


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        kSumCount = 0
        prefixSum = 0
        prefixMap = {0:1} #if there is a single element with k value, then it leads to using this
        for i in nums:
            prefixSum += i
            if prefixSum - k in prefixMap:
                # There is a prefix Array with 'prefixSum - k' sum that means if we subtract that from current prefixSum you will get k. 
                # And hence there is a subarray starting somewhere in the middle and ending at the current index for which the sum = k
                kSumCount += prefixMap[prefixSum - k]

            # Updating the current PrefixSum in the map
            prefixMap[prefixSum] = prefixMap.get(prefixSum, 0) + 1
        return kSumCount
