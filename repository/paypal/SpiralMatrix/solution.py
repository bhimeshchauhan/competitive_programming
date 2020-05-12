class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        # Initialize result
        result = []

        # Base Case
        if not matrix:
            return result

        # Reference First Column Row and Columns, Last Row and Column
        firstRow, firstCol, lastRow, lastCol = 0, 0, len(matrix) - 1, len(matrix[0]) - 1
        # Starting Direction
        dir = 'R'
        # Visited Rows Matrix
        seen = [[False] * len(matrix[0]) for _ in matrix]
        # while we are in bounds and in the same layer
        while (firstRow <= lastRow and firstCol <= lastCol):
            # Going right
            if dir == 'R':
                for i in range(firstCol, lastCol + 1):
                    if seen[firstRow][i] is False:
                        result.append(matrix[firstRow][i])
                        seen[firstRow][i] = True
                firstRow += 1
                # next go to down
                dir = 'D'

            # Going down
            if dir == 'D':
                for i in range(firstRow, lastRow + 1):
                    if seen[i][lastCol] is False:
                        result.append(matrix[i][lastCol])
                        seen[i][lastCol] = True
                lastCol -= 1
                # next go to left
                dir = 'L'

            # Going left
            if dir == 'L':
                for i in range(lastCol, firstCol - 1, -1):
                    if seen[lastRow][i] is False:
                        result.append(matrix[lastRow][i])
                        seen[lastRow][i] = True
                lastRow -= 1
                # next go to up
                dir = 'U'

            # Going up
            if dir == 'U':
                for i in range(lastRow, firstRow - 1, -1):
                    if seen[i][firstCol] is False:
                        result.append(matrix[i][firstCol])
                        seen[i][firstCol] = True
                firstCol += 1
                # next go to right
                dir = 'R'

        return result