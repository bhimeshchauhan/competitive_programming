"""

Given a positive integer n, generate an n x n matrix filled with elements from 1 to n2 in spiral order.

Example 1:

Input: n = 3
Output: [[1,2,3],[8,9,4],[7,6,5]]

Example 2:

Input: n = 1
Output: [[1]]

Constraints:

1 <= n <= 20

"""

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        if not n:
            return []
        res = [[0 for _ in range(n)] for _ in range(n)]
        left = 0
        right = n-1
        top = 0
        down = n-1 
        num = 1
        # If we have not touched the boundary
        while left <= right and top <= down:
            # all the way right
            for i in range(left, right+1):
                res[top][i] = num 
                num += 1
            top += 1
            # all the way down
            for i in range(top, down+1):
                res[i][right] = num
                num += 1
            right -= 1
            # all the way left
            for i in range(right, left-1, -1):
                res[down][i] = num
                num += 1
            down -= 1
            # all the way up
            for i in range(down, top-1, -1):
                res[i][left] = num
                num += 1
            left += 1
        return res
        