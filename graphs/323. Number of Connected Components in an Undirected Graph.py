# 323. Number of Connected Components in an Undirected Graph
# Solved
# Medium
# Topics
# Companies
# You have a graph of n nodes. You are given an integer n and an array edges where edges[i] = [ai, bi] indicates that there is an edge between ai and bi in the graph.

# Return the number of connected components in the graph.

 

# Example 1:


# Input: n = 5, edges = [[0,1],[1,2],[3,4]]
# Output: 2
# Example 2:


# Input: n = 5, edges = [[0,1],[1,2],[2,3],[3,4]]
# Output: 1
 

# Constraints:

# 1 <= n <= 2000
# 1 <= edges.length <= 5000
# edges[i].length == 2
# 0 <= ai <= bi < n
# ai != bi
# There are no repeated edges.

# Time Complexity: O(v+e)
# Space Complexity:O(v+e)
# Apprpach: 
# Iterate over each node, if a node is not visited,increment the ans by 1 (because its a connected component) and do dfs/bfs on that node to visit all the nodes in this component. 
# Once the dfs/bfs is completed, if we still encounter an unvisited node, that means its a different connected component, so increment the ans and continue with the dfs/bfs. 
# Do this until all the nodes are visited. Return the ans.


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = defaultdict(list)
        for each in edges:
            a, b = each[0], each[1]
            adj[a].append(b)
            adj[b].append(a)

        visited = set()
        def dfs(node):
            visited.add(node)
            st = [node]
            while st:
                n = st.pop()
                for i in adj[n]:
                    if i not in visited:
                        st.append(i)
                        visited.add(i)
        
        ans = 0
        for node in range(n):
            if node not in visited:
                dfs(node)
                ans += 1
        return ans
