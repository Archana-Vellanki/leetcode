# 189. Rotate Array
# Solved
# Medium
# Topics
# Companies
# Hint
# Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.


# Example 1:

# Input: nums = [1,2,3,4,5,6,7], k = 3
# Output: [5,6,7,1,2,3,4]
# Explanation:
# rotate 1 steps to the right: [7,1,2,3,4,5,6]
# rotate 2 steps to the right: [6,7,1,2,3,4,5]
# rotate 3 steps to the right: [5,6,7,1,2,3,4]
# Example 2:

# Input: nums = [-1,-100,3,99], k = 2
# Output: [3,99,-1,-100]
# Explanation:
# rotate 1 steps to the right: [99,-1,-100,3]
# rotate 2 steps to the right: [3,99,-1,-100]


# Constraints:

# 1 <= nums.length <= 105
# -231 <= nums[i] <= 231 - 1
# 0 <= k <= 105


# Follow up:

# Try to come up with as many solutions as you can. There are at least three different ways to solve this problem.
# Could you do it in-place with O(1) extra space?

# O(k) space:
# temp for k elements
# move the k elements to the end
# and then add temp to the beginning

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        temp = nums[-k:]
        # print(temp)
        nums[k:] = nums[:-k]
        # print(nums)
        nums[:k] = temp
        # print(nums)


# O(1) space:
# approach: consider the array [0,1,2,3,4,5,6],
# reverse the array=> [6,5,4,3,2,1,0]
# reverse the first k elements first ==> [5,6,4,3,2,1,0]
# then reverse the rest of the elements ==> [5,6,0,1,2,3,4]

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums.reverse()
        k = k % len(nums)

        left, right = 0, k-1
        while left < right:
            # print(left, right)
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
        # print(nums)
        left, right = k, len(nums) - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
        # print(nums)
