"""

Word Search

Given an m x n grid of characters board and a string word, 
return true if word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, 
where adjacent cells are horizontally or vertically neighboring. 
The same letter cell may not be used more than once.

Example 1:

Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
Output: true

Example 2:

Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
Output: true

Example 3:

Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
Output: false

Constraints:

m == board.length
n = board[i].length
1 <= m, n <= 6
1 <= word.length <= 15
board and word consists of only lowercase and uppercase English letters.

Follow up: Could you use search pruning to make your 
solution faster with a larger board?

"""

"""

Complexity Analysis

Time Complexity: O(n*3^L) where N is the number of cells in the board 
and L is the length of the word to be matched.

- For the backtracking function, initially we could have at most 4 directions
to explore, but further the choices are reduced into 3 (since we won't go back
to where we come from). As a result, the execution trace after the first step 
could be visualized as a 3-ary tree, each of the branches represent a potential 
exploration in the corresponding direction. Therefore, in the worst case, the total 
number of invocation would be the number of nodes in a full 3-nary tree, which is about 3^L

- We iterate through the board for backtracking, i.e. there could be N times 
invocation for the backtracking function in the worst case.

- As a result, overall the time complexity of the algorithm would be O(N⋅3^L).

Space Complexity: O(L) where L is the length of the word to be matched.

The main consumption of the memory lies in the recursion call of the backtracking 
function. The maximum length of the call stack would be the length of the word. 
Therefore, the space complexity of the algorithm is O(L).

"""


class Solution:
    def exist(self, board, word):
        if not board:
            return False
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.dfs(board, i, j, word):
                    return True
        return False

    # check whether can find word, start at (i,j) position
    def dfs(self, board, i, j, word):
        if len(word) == 0:  # all the characters are checked
            return True
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or word[0] != board[i][j]:
            return False
        tmp = board[i][j]  # first character is found, check the remaining part
        board[i][j] = "#"  # avoid visit agian
        # check whether can find "word" along one direction
        res = self.dfs(board, i+1, j, word[1:]) or self.dfs(board, i-1, j, word[1:]) \
            or self.dfs(board, i, j+1, word[1:]) or self.dfs(board, i, j-1, word[1:])
        board[i][j] = tmp
        return res
