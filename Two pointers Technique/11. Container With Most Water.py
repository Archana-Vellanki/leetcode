# 11. Container With Most Water
# Solved
# Medium
# Topics
# Companies
# Hint
# You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

# Find two lines that together with the x-axis form a container, such that the container contains the most water.

# Return the maximum amount of water a container can store.

# Notice that you may not slant the container.

 

# Example 1:


# Input: height = [1,8,6,2,5,4,8,3,7]
# Output: 49
# Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
# Example 2:

# Input: height = [1,1]
# Output: 1
 

# Constraints:

# n == height.length
# 2 <= n <= 105
# 0 <= height[i] <= 104

# Approach: start with two pointers one at 0 and other at the right end. Initialize a variable called maxi to keep track of the maximum capacity. 
# For every iteration increment the right or left pointer based on which line is shorter. For example if left line is shorter than the right one, 
# increase the left pointer by 1 else decrease the right pointer by 1. for every update calculate the current size and update maxi accordingly.

# Time complexity: O(n)

class Solution:
    def maxArea(self, height: List[int]) -> int:
        i, j = 0, len(height) - 1
        maxi = (j-i) * min(height[i], height[j])
        while i < j:
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
            size = (j-i) * min(height[i], height[j])
            if size > maxi:
                maxi = size
        return maxi
