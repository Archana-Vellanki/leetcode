# 261. Graph Valid Tree
# Solved
# Medium
# Topics
# Companies
# Hint
# You have a graph of n nodes labeled from 0 to n - 1. You are given an integer n and a list of edges where edges[i] = [ai, bi] indicates that there is an undirected edge between nodes ai and bi in the graph.

# Return true if the edges of the given graph make up a valid tree, and false otherwise.

 

# Example 1:


# Input: n = 5, edges = [[0,1],[0,2],[0,3],[1,4]]
# Output: true
# Example 2:


# Input: n = 5, edges = [[0,1],[1,2],[2,3],[1,3],[1,4]]
# Output: false
 

# Constraints:

# 1 <= n <= 2000
# 0 <= edges.length <= 5000
# edges[i].length == 2
# 0 <= ai, bi < n
# ai != bi
# There are no self-loops or repeated edges.

# Tree properties: 
# No cycles 
#   - Number of edges(e) == Number of nodes(v) - 1 
#   - if e < v: there are disconnected components
#   - if e > v: there are cycles 
# A node should be connected to any other node 
#   - after traversing(dfs/bfs) from a node, there shouldnt be any unvisited nodes. 
#   - If there are any unvisited nodes, that means there are disconnected components and hence not a valid tree
# For an edge (u,v) entry in adjacency list should be both ways, since it is an undirected graph.

# Time Complexity: O(v + e)
# Space Complexity: O(v) -- visited set
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        if len(edges) > n-1:
            return False # Loop 
        if len(edges) == 0:
            return n == 1 # If there are no edges, there should be just one node. If n is more than that, then there are two diconnected components and hence its not a valid tree
        adj = defaultdict(list)
        for each in edges:
            a,b =each[0], each[1]
            adj[a].append(b)
            adj[b].append(a)
        
        visited = set()
        def dfs(node):
            visited.add(node)
            for each in adj[node]:
                if each not in visited:
                    dfs(each)
        dfs(0)
        if len(visited) != n:
            return False
        return True
