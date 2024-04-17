# 977. Squares of a Sorted Array
# Solved
# Easy
# Topics
# Companies
# Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.


# Example 1:

# Input: nums = [-4,-1,0,3,10]
# Output: [0,1,9,16,100]
# Explanation: After squaring, the array becomes [16,1,0,9,100].
# After sorting, it becomes [0,1,9,16,100].
# Example 2:

# Input: nums = [-7,-3,2,3,11]
# Output: [4,9,9,49,121]


# Constraints:

# 1 <= nums.length <= 104
# -104 <= nums[i] <= 104
# nums is sorted in non-decreasing order.


# Follow up: Squaring each element and sorting the new array is very trivial, could you find an O(n) solution using a different approach?

# Approach: use two pointers to track the left and right most elements.
# those are the largest absoluate values.
# If we compare the absolute values, we will get to know which is the largest and square of that should be added to the end of the result array.
# move the left and right pointers accordingly and repeat the same steps till they reach the same point.

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        left, right = 0, len(nums) - 1
        result = [0]*(right + 1)
        i = right

        while left <= right:
            # print(left, right, i)
            if abs(nums[left]) >= abs(nums[right]):
                result[i] = nums[left] ** 2
                left += 1
            else:
                result[i] = nums[right] ** 2
                right -= 1
            i -= 1
        return result
