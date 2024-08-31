# 695. Max Area of Island
# Solved
# Medium
# Topics
# Companies
# You are given an m x n binary matrix grid. An island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

# The area of an island is the number of cells with a value 1 in the island.

# Return the maximum area of an island in grid. If there is no island, return 0.

 

# Example 1:


# Input: grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
# Output: 6
# Explanation: The answer is not 11, because the island must be connected 4-directionally.
# Example 2:

# Input: grid = [[0,0,0,0,0,0,0,0]]
# Output: 0
 

# Constraints:

# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 50
# grid[i][j] is either 0 or 1.

# Approach: for every new cell with 1, we will do BFS. With the iterative approach of BFS, we will cover all the connected cells with 1 and hence will increment the area for every cell in the queue.
# return the area and update the maxArea. 

# Time complexity: O(m*n)
# Space complexity: O(m*n)

class Solution:
    def bfs(self,i, j, visited, grid):
        visited.add((i,j))
        q = [(i,j)]
        dr, dc = [-1,1,0,0], [0,0,-1,1]
        area = 0
        while q:
            i, j = q.pop(0)
            area += 1
            for _ in range(4):
                r, c = i + dr[_], j + dc[_]
                if r >= 0 and r < len(grid) and c >= 0 and c < len(grid[0]) and grid[r][c] == 1 and (r,c) not in visited:
                    q.append((r,c))
                    visited.add((r,c))
        return area

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = set()
        maxArea = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1 and (i,j) not in visited:
                    maxArea = max(self.bfs(i, j, visited, grid), maxArea)
        return maxArea
