# 79. Word Search
# Medium
# 13.7K
# 555
# Companies
# Given an m x n grid of characters board and a string word, return true if word exists in the grid.

# The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.


# Example 1:


# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
# Output: true
# Example 2:


# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
# Output: true
# Example 3:


# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
# Output: false


# Constraints:

# m == board.length
# n = board[i].length
# 1 <= m, n <= 6
# 1 <= word.length <= 15
# board and word consists of only lowercase and uppercase English letters.


# Follow up: Could you use search pruning to make your solution faster with a larger board?


# Time complexity: O(m*n*4^L)
# Space complexity: O(L)

# Approach: use DFS. All other approaches I used are exceeding the time limit at least in 1 test case(mentioned one in the commented section below). this is the optimized solution.
class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """

        length = len(word)
        rows, cols = len(board), len(board[0])
        visited = set()

        def dfs(r, c, i):
            if i == length:
                return True
            if r < 0 or c < 0 or r >= rows or c >= cols or (r, c) in visited or word[i] != board[r][c]:
                return False

            visited.add((r, c))

            res = (dfs(r-1, c, i+1) or
                   dfs(r, c-1, i+1) or
                   dfs(r+1, c, i+1) or
                   dfs(r, c+1, i+1))
            visited.remove((r, c))
            return res

        for i in range(rows):
            for j in range(cols):
                if dfs(i, j, 0):
                    return True

        return False


# class Solution(object):
#     def exist(self, board, word):
#         """
#         :type board: List[List[str]]
#         :type word: str
#         :rtype: bool
#         """

#         length = len(word)
#         rows, cols = len(board), len(board[0])
#         visited = set()

#         def findNeighbours(i, j, k):
#             arr = []
#             m = [ 1, 0, -1, 0]
#             n = [ 0, 1, 0, -1]
#             for _ in range(4):
#                 if i + m[_] < rows and i + m[_] >= 0 and j + n[_] < cols and j + n[_] >= 0:
#                     arr.append((i + m[_], j + n[_], k))
#             # print("neighbours of ", board[i][j], "are", arr)
#             return arr


#         def dfs(r,c,i):
#             # print(r,c,i)
#             if i == length:
#                 return True
#             if (r,c) in visited or word[i] != board[r][c]:
#                 return False

#             visited.add((r,c))
#             nei = findNeighbours(r,c,i+1)
#             if nei:
#                 res = any([dfs(m,n,k) for (m,n,k) in nei])
#             else:
#                 return i+1 == length
#             visited.remove((r,c))
#             return res

#         for i in range(rows):
#             for j in range(cols):
#                 # if board[i][j] == word[0]:
#                 if dfs(i, j, 0): return True

#         return False
