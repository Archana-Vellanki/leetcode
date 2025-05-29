# 42. Trapping Rain Water
# Solved
# Hard
# Topics
# premium lock icon
# Companies
# Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

 

# Example 1:


# Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
# Output: 6
# Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.
# Example 2:

# Input: height = [4,2,0,3,2,5]
# Output: 9
 

# Constraints:

# n == height.length
# 1 <= n <= 2 * 104
# 0 <= height[i] <= 105

# Most Optimized approach
# Water is trapped between bars and the smaller bar will limit the amount of water trapped.
# Hence maintain two vars for left_max and right_max heights. Update them as we iterate over each height.
# Take the min of the left_max and right_max, as this is going to limit the amount of water trapped, and subtract the height of the current bar from it. This gives the amount of water

class Solution:
    def trap(self, height: List[int]) -> int:
        left_max = 0
        right_max = 0
        left, right = 0, len(height) - 1
        water = 0
        while left < right:
            left_max = max(left_max, height[left])
            right_max = max(height[right], right_max)
            if left_max < right_max:
                water += left_max - height[left]
                left += 1
            else:
                water += right_max - height[right]
                right -= 1

        return water

# My bruteforce approach
# Extra space used:O(n)
class Solution:
    def trap(self, height: List[int]) -> int:
        # [0,1,0,2,1,0,1,3,2,1,2,1]
        # [0,1,1,2,2,2,2,3,3,3,3,3]
        # [3,3,3,3,3,3,3,3,2,2,2,1]
        l = len(height)
        left_max = 0
        left_heights = [0]*l
        for i in range(l):
            left_max = max(left_max, height[i])
            left_heights[i] = left_max
        ans = 0
        right_max = 0
        # print(left_heights)
        for j in range(l-1, -1, -1):
            right_max = max(right_max, height[j])
            water = min(right_max, left_heights[j]) - height[j]
            if water > 0:
                ans += water
        return ans
