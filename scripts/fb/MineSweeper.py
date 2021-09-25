"""

Minesweeper

Let's play the minesweeper game (Wikipedia, online game)!

You are given an m x n char matrix board representing the game board where:

'M' represents an unrevealed mine,
'E' represents an unrevealed empty square,
'B' represents a revealed blank square that has no adjacent mines 
(i.e., above, below, left, right, and all 4 diagonals),
digit ('1' to '8') represents how many mines are adjacent to this revealed square, and
'X' represents a revealed mine.
You are also given an integer array click where click = [clickr, clickc] 
represents the next click position among all the unrevealed squares ('M' or 'E').

Return the board after revealing this position according to the following rules:

If a mine 'M' is revealed, then the game is over. You should change it to 'X'.
If an empty square 'E' with no adjacent mines is revealed, then change it to a 
revealed blank 'B' and all of its adjacent unrevealed squares should be revealed recursively.
If an empty square 'E' with at least one adjacent mine is revealed, 
then change it to a digit ('1' to '8') representing the number of adjacent mines.
Return the board when no more squares will be revealed.

Example 1:

Input: board = [["E","E","E","E","E"],["E","E","M","E","E"],["E","E","E","E","E"],["E","E","E","E","E"]], click = [3,0]
Output: [["B","1","E","1","B"],["B","1","M","1","B"],["B","1","1","1","B"],["B","B","B","B","B"]]

Example 2:

Input: board = [["B","1","E","1","B"],["B","1","M","1","B"],["B","1","1","1","B"],["B","B","B","B","B"]], click = [1,2]
Output: [["B","1","E","1","B"],["B","1","X","1","B"],["B","1","1","1","B"],["B","B","B","B","B"]]

Constraints:

m == board.length
n == board[i].length
1 <= m, n <= 50
board[i][j] is either 'M', 'E', 'B', or a digit from '1' to '8'.
click.length == 2
0 <= clickr < m
0 <= clickc < n
board[clickr][clickc] is either 'M' or 'E'.


"""

"""

If current click is not 'M', we need to sweep its surroundings and 
decide whether to recursive search or not.

If there is at least one mine at 8 surrounding cells, we stop recursive 
search for this cell and mark it as the number of surrounding mines. 
Otherwise, we DFS on this cell and mark it as 'B'. Next level searching 
cell would be one of 8 surrounding cells.

"""


class Solution:
    def updateBoard(self, board, click):
        i, j, m, n = *click, len(board), len(board[0])

        def dfs(i, j):
            if board[i][j] == 'E':
                neis = [(x, y) for x, y in ((i-1, j-1), (i-1, j), (i-1, j+1), (i, j-1), (i, j+1), (i+1, j-1), (i+1, j), (i+1, j+1))
                        if 0 <= x < m and 0 <= y < n]
                cnt = sum(board[x][y] == 'M' for x, y in neis)
                if not cnt:
                    board[i][j] = 'B'
                    for x, y in neis:
                        dfs(x, y)
                else:
                    board[i][j] = str(cnt)
        if board[i][j] == 'M':
            board[i][j] = 'X'
        else:
            dfs(i, j)
        return board
