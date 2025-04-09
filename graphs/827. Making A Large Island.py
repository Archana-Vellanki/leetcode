# 827. Making A Large Island
# Solved
# Hard
# Topics
# Companies
# You are given an n x n binary matrix grid. You are allowed to change at most one 0 to be 1.

# Return the size of the largest island in grid after applying this operation.

# An island is a 4-directionally connected group of 1s.

 

# Example 1:

# Input: grid = [[1,0],[0,1]]
# Output: 3
# Explanation: Change one 0 to 1 and connect two 1s, then we get an island with area = 3.
# Example 2:

# Input: grid = [[1,1],[1,0]]
# Output: 4
# Explanation: Change the 0 to 1 and make the island bigger, only one island with area = 4.
# Example 3:

# Input: grid = [[1,1],[1,1]]
# Output: 4
# Explanation: Can't change any 0 to 1, only one island with area = 4.
 

# Constraints:

# n == grid.length
# n == grid[i].length
# 1 <= n <= 500
# grid[i][j] is either 0 or 1.
# Intuition is mentioned in the docstring below

# Implementation:
# 1. Labeling Islands: 
#     Explore each island (a group of connected 1's) using BFS and label every cell with a unique island identifier.
#     Also, compute and store the area (number of cells) for each island.
# 2. Calculating Maximum Area by Flipping a 0:
#     For every water cell (0), check its four adjacent cells. If any adjacent cell is part of an island,
#     use a set to collect unique island labels and sum the areas of these islands plus one (for the flipped cell).
# 3. The answer is the maximum island area found either from the original islands or by a combination when flipping one water cell.

# Time complexity: O(n*n) where n is the number of rows and cols
# Space complexity: O(n*n) where n is the number of rows and cols (for visited set, island_map)

class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        '''
        any 0 with atleast an adjacent 1 is considerable.
        if it has 2 adjacent 1s even better but they should not belong to the same island (they both should not be neighbours)
        Which Data Structures can be used here to be able to answer these questions: 
         - which island does (r,c) belong to and what is the area of it?
         - how can we group islands and search for a cell fastly?

         Island_map: (r,c): Island_number
         Island_area: island_number: area
         
        '''
        island_count = 0 # Total number of islands we explored
        island_map = {} # each (r,c) is labelled with the island_number
        island_area = {} # area of each island
        n= len(grid)
        adj = [(0,1), (0,-1), (1,0), (-1,0)]
        visited = set()

        def helper_bfs(r,c):
            nonlocal island_count
            nonlocal n
            area = 0
            q = deque()
            q.append((r,c))
            visited.add((r,c))
            island_map[(r,c)] = island_count
            while q:
                ro, col = q.popleft()
                area += 1
                for _ in range(4):
                    nr, nc = ro + adj[_][0], col + adj[_][1]
                    if 0 <= nr < n and 0 <= nc < n and (nr,nc) not in visited and grid[nr][nc] == 1:
                        visited.add((nr,nc))
                        q.append((nr,nc))
                        island_map[(nr,nc)] = island_count
            island_area[island_count] = area
            area = 0
            island_count += 1
        # Labelling islands and computing the area for each island
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1 and (i, j) not in visited:
                    helper_bfs(i,j)
        # print(island_map, island_area, "\n ds ready")
      
        if not island_count:
            return 1
        
        # Explore every 0 cell and find out by flipping which one we would get maximum area
        max_area = max(island_area.values())
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 0:
                    adjIslands = set()
                    for _ in range(4):
                        nr, nc = i + adj[_][0], j + adj[_][1]
                        if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] == 1:
                            adjIslands.add(island_map[(nr,nc)])
                    if len(adjIslands) >= 1:
                        max_area = max(max_area, sum([island_area[_] for _ in adjIslands]) + 1)
        return max_area

