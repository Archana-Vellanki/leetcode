# 289. Game of Life
# Medium

# According to Wikipedia's article: "The Game of Life, also known simply as Life, is a cellular automaton devised by the British mathematician John Horton Conway in 1970."

# The board is made up of an m x n grid of cells, where each cell has an initial state: live (represented by a 1) or dead (represented by a 0).
# Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) using the following four rules (taken from the above Wikipedia article):

# Any live cell with fewer than two live neighbors dies as if caused by under-population.
# Any live cell with two or three live neighbors lives on to the next generation.
# Any live cell with more than three live neighbors dies, as if by over-population.
# Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
# The next state is created by applying the above rules simultaneously to every
# cell in the current state, where births and deaths occur simultaneously. Given the current state of the m x n grid board, return the next state.


# Example 1:


# Input: board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
# Output: [[0,0,0],[1,0,1],[0,1,1],[0,1,0]]
# Example 2:


# Input: board = [[1,1],[1,0]]
# Output: [[1,1],[1,1]]


# Constraints:

# m == board.length
# n == board[i].length
# 1 <= m, n <= 25
# board[i][j] is 0 or 1.


# Follow up:

# Could you solve it in-place? Remember that the board needs to be updated simultaneously:
# You cannot update some cells first and then use their updated values to update other cells.
# In this question, we represent the board using a 2D array. In principle, the board is infinite,
# which would cause problems when the active area encroaches upon the border of the array (i.e., live cells reach the border). How would you address these problems?


# time complexity: O(m*n)
# Space complexity: O(m*n)
class Solution(object):
    def neighbours(self, ro, col, board):
        # Finding the neighbours of a given cell by checking the boundaries
        adj = []
        ros, cols = len(board), len(board[0])
        i = [-1, -1, -1, 0, 0, 1, 1, 1]
        j = [-1, 0, 1, -1, 1, -1, 0, 1]
        for each in range(8):
            r = ro + i[each]
            c = col + j[each]
            if r >= 0 and r < ros and c >= 0 and c < cols:
                adj.append((r, c))
        return adj

    def findNextState(self, adj, ro, col, board):
        # based on the live neighbours count, find the next state of the current cell
        liveNeighbourCount = 0
        nextState = board[ro][col]
        for each in adj:
            if board[each[0]][each[1]] == 1:
                liveNeighbourCount += 1
        if board[ro][col] == 0:
            if liveNeighbourCount == 3:
                nextState = 1
        else:
            if liveNeighbourCount < 2:
                nextState = 0
            elif liveNeighbourCount == 2 or liveNeighbourCount == 3:
                nextState = 1
            elif liveNeighbourCount > 3:
                nextState = 0
        return nextState

    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        stateChanges = {}
        for i in range(len(board)):
            for j in range(len(board[0])):
                # for each cell find out the neighbours and th next State
                # store the next state of each cell in a dictionary with the indices tuple as the key and next state as value
                adj = self.neighbours(i, j, board)
                nextState = self.findNextState(adj, i, j, board)
                if nextState != board[i][j]:
                    tup = (i, j)
                    stateChanges[(tup)] = nextState
        # iterate only through the changed states dictionary and change them in place
        for ind, state in stateChanges.items():
            board[ind[0]][ind[1]] = state
        return board
