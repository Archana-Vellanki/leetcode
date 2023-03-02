# 62. Unique Paths
# Medium

# There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.

# Given the two integers m and n, return the number of possible unique paths that the robot can take to reach the bottom-right corner.

# The test cases are generated so that the answer will be less than or equal to 2 * 109.

# Example 1:

# Input: m = 3, n = 7
# Output: 28
# Example 2:

# Input: m = 3, n = 2
# Output: 3
# Explanation: From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
# 1. Right -> Down -> Down
# 2. Down -> Down -> Right
# 3. Down -> Right -> Down


# Constraints:

# 1 <= m, n <= 100

class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        # Space complexity = O(m*n)
        # Time complexity = O(m*n)
        if m == 1 or n == 1:
            return 1

        grid = [[0 for i in range(n)] for j in range(m)]

        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                if i == m-1 or j == n-1:
                    grid[i][j] = 0 if i == m-1 and j == n-1 else 1
                else:
                    grid[i][j] = grid[i+1][j] + grid[i][j+1]

        return grid[0][0]

# Better approach:
    # Space complexity = O(n)
    # Time Complexity = O(mn)


class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """

        if m == 1 or n == 1:
            return 1
        ro = [1]*n
        for i in range(1, m):
            for j in range(1, n):
                ro[j] += ro[j - 1]
        return ro[-1]


# Better approach:
    # Space Complexity: O(1)
    # Time Complexity: O(min(m, n))
# This approach uses a combinatorial solution that involves the fact that the number of unique paths is the same as the number of combinations of steps.
# We calculate the number of steps required to reach the destination cell (m+n-2),
# and then calculate the number of combinations of m-1 steps (or n-1 steps) out of the total steps.

class Solution(object):
    def uniquePaths(self, m, n):
        # calculate number of steps required to reach destination cell
        steps = m + n - 2

        # calculate number of combinations of m-1 steps or n-1 steps
        combinations = 1
        for i in range(1, min(m, n)-1):
            combinations *= (steps-i)
            combinations //= i

        return combinations
