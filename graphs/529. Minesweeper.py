# 529. Minesweeper
# Solved
# Medium
# Topics
# Companies
# Let's play the minesweeper game (Wikipedia, online game)!

# You are given an m x n char matrix board representing the game board where:

# 'M' represents an unrevealed mine,
# 'E' represents an unrevealed empty square,
# 'B' represents a revealed blank square that has no adjacent mines (i.e., above, below, left, right, and all 4 diagonals),
# digit ('1' to '8') represents how many mines are adjacent to this revealed square, and
# 'X' represents a revealed mine.
# You are also given an integer array click where click = [clickr, clickc] represents the next click position among all the unrevealed squares ('M' or 'E').

# Return the board after revealing this position according to the following rules:

# If a mine 'M' is revealed, then the game is over. You should change it to 'X'.
# If an empty square 'E' with no adjacent mines is revealed, then change it to a revealed blank 'B' and all of its adjacent unrevealed squares should be revealed recursively.
# If an empty square 'E' with at least one adjacent mine is revealed, then change it to a digit ('1' to '8') representing the number of adjacent mines.
# Return the board when no more squares will be revealed.
 

# Example 1:
# Input: board = [["E","E","E","E","E"],["E","E","M","E","E"],["E","E","E","E","E"],["E","E","E","E","E"]], click = [3,0]
# Output: [["B","1","E","1","B"],["B","1","M","1","B"],["B","1","1","1","B"],["B","B","B","B","B"]]

# Example 2:
# Input: board = [["B","1","E","1","B"],["B","1","M","1","B"],["B","1","1","1","B"],["B","B","B","B","B"]], click = [1,2]
# Output: [["B","1","E","1","B"],["B","1","X","1","B"],["B","1","1","1","B"],["B","B","B","B","B"]]
 

# Constraints:

# m == board.length
# n == board[i].length
# 1 <= m, n <= 50
# board[i][j] is either 'M', 'E', 'B', or a digit from '1' to '8'.
# click.length == 2
# 0 <= clickr < m
# 0 <= clickc < n
# board[clickr][clickc] is either 'M' or 'E'.

# Intuition:
# Mine Check: Immediately handle the clicked mine and return.
# Reveal Safe Areas: For empty cells without adjacent mines, reveal them and let the "ripple" reveal neighboring cells.
# Boundaries: Stop the ripple where numbers appear since these cells indicate danger.
# Use BFS (or a similar method) to ensure every safe cell is processed without repeats.


# Time Complexity: every cell in the board is processed exactly once- O(m * n)
# Space Complexity: In the worst-case, the queue and visited set could store almost all cells- O(m * n).

class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]: 
        if board[click[0]][click[1]] == 'M':                
            board[click[0]][click[1]] = 'X'
            return board
        
        m, n = len(board), len(board[0])
        adj = [(0,1),(-1,1),(1,1),(-1,0),(1,0),(0,-1),(1,-1),(-1,-1)]
        q = deque()
        visited = set()
        visited.add(tuple(click))
        q.append(click)
        while q:
            r, c = q.popleft()
            m_count = 0
            for each in adj:
                dr, dc = r + each[0], c + each[1]
                if 0 <= dr < m and 0 <=dc < n and board[dr][dc] == 'M':
                        m_count += 1
                
            if m_count != 0:
                # at least one adjacent mine
                board[r][c] = str(m_count)
                # visited.add((r,c))
            else:
                # no adjacent mines
                board[r][c] = 'B'
                for each in adj:
                    dr, dc = r + each[0], c + each[1]
                    if 0 <= dr < m and 0 <=dc < n and (dr,dc) not in visited and board[dr][dc] == 'E':
                        visited.add((dr,dc))
                        q.append((dr,dc))
        return board
        
