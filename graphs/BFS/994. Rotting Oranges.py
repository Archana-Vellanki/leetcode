# 994. Rotting Oranges
# Solved
# Medium
# Topics
# Companies
# You are given an m x n grid where each cell can have one of three values:

# 0 representing an empty cell,
# 1 representing a fresh orange, or
# 2 representing a rotten orange.
# Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

# Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.

# Example 1:

# Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
# Output: 4
# Example 2:

# Input: grid = [[2,1,1],[0,1,1],[1,0,1]]
# Output: -1
# Explanation: The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.
# Example 3:

# Input: grid = [[0,2]]
# Output: 0
# Explanation: Since there are already no fresh oranges at minute 0, the answer is just 0.
 

# Constraints:

# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 10
# grid[i][j] is 0, 1, or 2.


# Approach: Regular BFS might lead to incorrect solution because it processes the rotten oranges consecutively by completely rotting the oranges 
# connecting to one rotten orange before visiting the next rotten orange. but to achieve the minimum number of minutes, we need the rotting process to start from all initially rotten oranges simultaneously. 
# Hence before starting the BFS, add all the initial rotten oranges to the queue. Then pop the rotten orange from the queue, rot the adjacent oranges 
# and add them to the queue. By doing this we will ensure that rotting process starts from all the rotting oranges simultaneously and hence results in minimum number
# of minutes. 

# Example: Consider this example [[2,1,1],[1,1,1],[0,1,2]]. With regular bfs, we will visit all oranges adjacent to the first rotten orange 
# and Only after completely visiting these would we move to the second rotten orange (2) at the opposite corner. 
# we will visit the second 2 but the oranges adjacent to second 2 will take longer time. because the rotting process starts from here as well. 
# so by adding both the rotten orangews to the queue initially, BFS processes the neighbours of both at the same time,
# there by ensuring minimum number of minutes.

# Time complexity: O(m*n) m =rows, n=cols
# Space complexity:O(m*n) m =rows, n=cols

from collections import deque

class Solution:
    def bfs(self, grid, visited):
        q = deque()
        minutes = 0
        dr = [1, -1, 0, 0]
        dc = [0, 0, 1, -1]

        # Add all initial rotten oranges to the queue
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    q.append((i, j, 0))
                    visited[(i, j)] = 0
        
        while q:
            r, c, mins = q.popleft()
            for k in range(4):
                nr, nc = r + dr[k], c + dc[k]
                if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and grid[nr][nc] == 1:
                    grid[nr][nc] = 2
                    q.append((nr, nc, mins + 1))
                    visited[(nr, nc)] = mins + 1
                    minutes = max(minutes, mins + 1)
        
        return minutes

    def orangesRotting(self, grid: List[List[int]]) -> int:
        visited = {}
        minutes = self.bfs(grid, visited)
        
        # Check if there's any fresh orange left
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    return -1
        return minutes

