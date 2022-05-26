from typing import List


class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

#         1 -> 0 = -1 ( consider while neighbour counting one's)
#         0 -> 1 = -2 (don't consider while neighbour counting one's)

        for row in range(len(board)):
            for column in range(len(board[0])):
                neighbour_count = 0
                val = board[row][column]
                for r, c in [[-1, 0], [1, 0], [0, -1], [0, 1], [-1, -1], [-1, 1], [1, -1], [1, 1]]:
                    if 0 <= row+r < len(board) and 0 <= column+c < len(board[0]):
                        new_row, new_column = row+r, column+c
                        if abs(board[new_row][new_column]) == 1:
                            neighbour_count += 1
                if neighbour_count < 2 and abs(val) == 1:
                    board[row][column] = -1
                elif neighbour_count > 3 and abs(val) == 1:
                    board[row][column] = -1
                elif neighbour_count == 3 and abs(val) == 0:
                    board[row][column] = -2

#       converting all -1 to 0
#       converting all -2 to 1

        for row in range(len(board)):
            for column in range(len(board[0])):
                if board[row][column] == -1:
                    board[row][column] = 0
                elif board[row][column] == -2:
                    board[row][column] = 1


class Solution(object):
    def gameOfLife(self, board):

        top_row = [0] * len(board[0])

        for i in range(len(board)):

            # copy the current row for updating next row
            temp_row = [ele for ele in board[i]]

            # get the bottom row
            if i == len(board) - 1:
                botton_row = [0] * len(board[0])
            else:
                botton_row = board[i+1]

            # get the left element
            left = 0

            for j in range(len(board[0])):
                # copy the current value for updating the next element
                temp_left = board[i][j]

                # count neighbors
                if 0 < j < len(board[0]) - 1:
                    ssum = sum(top_row[j-1:j+2]) + left + \
                        board[i][j+1] + sum(botton_row[j-1:j+2])

                elif j == len(board[0]) - 1:
                    ssum = sum(top_row[j-1:j+1]) + left + \
                        sum(botton_row[j-1:j+1])

                else:
                    ssum = sum(top_row[:j+2]) + \
                        board[i][j+1] + sum(botton_row[:j+2])

                # update the current position
                if board[i][j]:
                    if ssum < 2 or ssum > 3:
                        board[i][j] = 0
                else:
                    if ssum == 3:
                        board[i][j] = 1

                # update the left element value for next element in board
                left = temp_left

            # update the top row for next row in board
            top_row = temp_row
