"""

You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. 
DO NOT allocate another 2D matrix and do the rotation.

Example 1:

Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [[7,4,1],[8,5,2],[9,6,3]]

Example 2:

Input: matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
Output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]

Example 3:

Input: matrix = [[1]]
Output: [[1]]

Example 4:

Input: matrix = [[1,2],[3,4]]
Output: [[3,1],[4,2]] 

Constraints:

matrix.length == n
matrix[i].length == n
1 <= n <= 20
-1000 <= matrix[i][j] <= 1000

00 01 02 03 04
10 11 12 13 14
20 21 22 23 24
30 31 32 33 34
40 41 42 43 44

=>

40 30 20 10 00
41 31 21 11 01
42 32 22 12 02
43 33 23 13 03
44 34 24 14 04

algo->
savingin temp 4 0
4 0  ->  4 4
4 4  ->  0 4
0 4  ->  0 0
0 0  ->  4 0
savingin temp 3 0
3 0  ->  4 3
4 3  ->  1 4
1 4  ->  0 1
0 1  ->  3 0
savingin temp 4 1
4 1  ->  3 4
3 4  ->  0 3
0 3  ->  1 0
1 0  ->  4 1
savingin temp 3 1
3 1  ->  3 3
3 3  ->  1 3
1 3  ->  1 1
1 1  ->  3 1
savingin temp 4 2
4 2  ->  2 4
2 4  ->  0 2
0 2  ->  2 0
2 0  ->  4 2
savingin temp 3 2
3 2  ->  2 3
2 3  ->  1 2
1 2  ->  2 1
2 1  ->  3 2

"""

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        self.transpose(matrix)
        self.reflect(matrix)
    
    def transpose(self, matrix):
        n = len(matrix)
        for i in range(n):
            for j in range(i, n):
                matrix[j][i], matrix[i][j] = matrix[i][j], matrix[j][i]

    def reflect(self, matrix):
        n = len(matrix)
        for i in range(n):
            for j in range(n // 2):
                print('reflect ', i, j, -j-1)
                matrix[i][j], matrix[i][-j - 1] = matrix[i][-j - 1], matrix[i][j]
