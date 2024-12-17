# 219. Contains Duplicate II
# Solved
# Easy
# Topics
# Companies
# Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.

 

# Example 1:

# Input: nums = [1,2,3,1], k = 3
# Output: true
# Example 2:

# Input: nums = [1,0,1,1], k = 1
# Output: true
# Example 3:

# Input: nums = [1,2,3,1,2,3], k = 2
# Output: false
 

# Constraints:

# 1 <= nums.length <= 105
# -109 <= nums[i] <= 109
# 0 <= k <= 105

# Approach 1: Keep track of each element and its index in a hashmap. If an element is already in the hashmap, 
# check if the difference between the current index and the index stored is <= k,if so return True. Else return False
# everytime update the latest index of the element

# Time complexity: O(n)
# Space complexity: O(n)

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hashmap = {}
        for i in range(len(nums)):
            if nums[i] not in hashmap:
                hashmap[nums[i]] = i
            else:
                if abs(i - hashmap[nums[i]]) <= k:
                    return True
                hashmap[nums[i]] = i
        return False
# Approach 2: Store only the current window elements. pop the older elements
# Time complexity: O(n)
# Space complexity: O(k)
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        length = len(nums)
        if length <= 1:
            return False
        i = 0
        j = 1
        hashmap = {nums[i]}
        while j < length:
            # print(i,j,hashmap)
            if abs(i - j) <= k:
                if nums[j] in hashmap:
                    return True
                else:
                    hashmap.add(nums[j])
                    j += 1
            else:
                hashmap.remove(nums[i])
                i += 1
        return False
