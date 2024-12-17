# 35. Search Insert Position
# Solved
# Easy
# Topics
# Companies
# Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

# You must write an algorithm with O(log n) runtime complexity.

 

# Example 1:

# Input: nums = [1,3,5,6], target = 5
# Output: 2
# Example 2:

# Input: nums = [1,3,5,6], target = 2
# Output: 1
# Example 3:

# Input: nums = [1,3,5,6], target = 7
# Output: 4
 

# Constraints:

# 1 <= nums.length <= 104
# -104 <= nums[i] <= 104
# nums contains distinct values sorted in ascending order.
# -104 <= target <= 104

# Approach: since log(n) time complexity is required, binary search is the go to approach. 
# Updating i to mid +1 because  the target can never be inserted at a smaller element's position. 
# Updating j to mid because j can be the next higher position where the target has to be inserted. 

# Time complexity: O(logn)
# Space complexity: O(1)
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        i = 0
        j = len(nums) - 1
        if nums[j] < target:
            return j + 1
        
        while i < j:
            mid = (i + j) //2
            if nums[mid] > target:
                j = mid
            elif nums[mid] < target:
                i = mid +1
            else:
                return mid
        return i
