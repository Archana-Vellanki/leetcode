# 417. Pacific Atlantic Water Flow
# Medium
# 6.6K
# 1.3K
# Companies
# There is an m x n rectangular island that borders both the Pacific Ocean and Atlantic Ocean. The Pacific Ocean touches the island's left and top edges, and the Atlantic Ocean touches the island's right and bottom edges.

# The island is partitioned into a grid of square cells. You are given an m x n integer matrix heights where heights[r][c] represents the height above sea level of the cell at coordinate (r, c).

# The island receives a lot of rain, and the rain water can flow to neighboring cells directly north, south, east, and west if the neighboring cell's height is less than or equal to the current cell's height. Water can flow from any cell adjacent to an ocean into the ocean.

# Return a 2D list of grid coordinates result where result[i] = [ri, ci] denotes that rain water can flow from cell (ri, ci) to both the Pacific and Atlantic oceans.


# Example 1:


# Input: heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
# Output: [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]
# Explanation: The following cells can flow to the Pacific and Atlantic oceans, as shown below:
# [0,4]: [0,4] -> Pacific Ocean
#        [0,4] -> Atlantic Ocean
# [1,3]: [1,3] -> [0,3] -> Pacific Ocean
#        [1,3] -> [1,4] -> Atlantic Ocean
# [1,4]: [1,4] -> [1,3] -> [0,3] -> Pacific Ocean
#        [1,4] -> Atlantic Ocean
# [2,2]: [2,2] -> [1,2] -> [0,2] -> Pacific Ocean
#        [2,2] -> [2,3] -> [2,4] -> Atlantic Ocean
# [3,0]: [3,0] -> Pacific Ocean
#        [3,0] -> [4,0] -> Atlantic Ocean
# [3,1]: [3,1] -> [3,0] -> Pacific Ocean
#        [3,1] -> [4,1] -> Atlantic Ocean
# [4,0]: [4,0] -> Pacific Ocean
#        [4,0] -> Atlantic Ocean
# Note that there are other possible paths for these cells to flow to the Pacific and Atlantic oceans.
# Example 2:

# Input: heights = [[1]]
# Output: [[0,0]]
# Explanation: The water can flow from the only cell to the Pacific and Atlantic oceans.


# Constraints:

# m == heights.length
# n == heights[r].length
# 1 <= m, n <= 200
# 0 <= heights[r][c] <= 105


# Time complexity: O(m + n)
# Space complexity: O(m + n)

# Approach: Instead of going to every cell and doing DFS to see if it reaches the ocean, try DFS from the border cells to other cells.
# Since we are doing the reverse, the height of the neighbour should be greater than the current cell to consider the neighbour
class Solution(object):
    def pacificAtlantic(self, heights):
        """
        :type heights: List[List[int]]
        :rtype: List[List[int]]
        """
        rows = len(heights)
        cols = len(heights[0])

        pacific = set()
        atlantic = set()

        def neighbours(row, col):
            m = [0, -1, 0, 1]
            n = [-1, 0, 1, 0]
            nei = []
            for i in range(4):
                if row+m[i] < rows and row+m[i] >= 0 and col+n[i] < cols and col+n[i] >= 0:
                    nei.append((row + m[i], col + n[i]))
            return nei

        def dfs(ro, col, prevHeight, visited):
            if (ro, col) in visited or heights[ro][col] < prevHeight:
                return
            visited.add((ro, col))
            for each in neighbours(ro, col):
                dfs(each[0], each[1], heights[ro][col], visited)

        # start from the first and last rows for pacific and atlantic oceans respectively
        for i in range(rows):
            dfs(i, 0, heights[i][0], pacific)
            dfs(i, cols - 1, heights[i][cols - 1], atlantic)

        # start from the first and last columns for pacific and atlantic oceans respectively
        for j in range(cols):
            dfs(0, j, heights[0][j], pacific)
            dfs(rows - 1, j, heights[rows - 1][j], atlantic)
        return pacific.intersection(atlantic)
