# 200. Number of Islands
# Solved
# Medium
# Topics
# Companies
# Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

# An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

 

# Example 1:

# Input: grid = [
#   ["1","1","1","1","0"],
#   ["1","1","0","1","0"],
#   ["1","1","0","0","0"],
#   ["0","0","0","0","0"]
# ]
# Output: 1
# Example 2:

# Input: grid = [
#   ["1","1","0","0","0"],
#   ["1","1","0","0","0"],
#   ["0","0","1","0","0"],
#   ["0","0","0","1","1"]
# ]
# Output: 3
 

# Constraints:

# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 300
# grid[i][j] is '0' or '1'.

# Approach: BFS makes more sense than DFS because it completes each layer by layer near the starting 1 node. Used Iterative approach by using queue and a visited list.
# Iterate through each node, if it is 1 and not visited till now, it means we have found a new land and hence increase the number of islands by 1. 
# Then we will BFS from that node to cover all the connected 1's i.e. land pieces. 
# If it is 0 continue. 
# Inside the BFS:
# maintain a queue to keep track of the neighbours yet to be visited.
# add the current node to the queue. 
# while the queue is not empty, pop each node add its neighbours to the queue and visited list. while adding the neighbours, make sure to add only the unvisited land pieces(1's) else you might end up in an infinite loop.
# By the end of BFS, we would have covered all the connected 1's. for the current node.
# Similarly we will continue this process for every node in the grid.

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        numOfIslands = 0
        visited = set()
        

        def bfs(i, j):
            # print(i, j)
            q = []
            
            q.append((i,j))
            visited.add((i, j))

            while len(q) != 0:
                # print(q)
                r,c = q.pop(0)
                # neighbors
                dr = [1, -1, 0, 0]
                dc = [0, 0, 1, -1]
                for _ in range(4):
                    nei_r = r + dr[_]
                    nei_c = c + dc[_]
                    # print(nei_r, nei_c)
                    if (nei_r >=0 and nei_r < rows and nei_c >= 0 and nei_c < cols and (nei_r, nei_c) not in visited):
                        if (grid[nei_r][nei_c] == "1"):
                            q.append((nei_r, nei_c))
                            visited.add((nei_r, nei_c))

        for x in range(rows):
            for y in range(cols):
                if grid[x][y] == "1" and (x,y) not in visited:
                    numOfIslands += 1
                    bfs(x, y)
        
        return numOfIslands
            

            


        