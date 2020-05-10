"""
Example Walk Through
- Params
    s = "PAYPALISHIRING"
    numRows = 3

    Solution().convert("PAYPALISHIRING", 3)

- Constant Variables
    - numRows - 1 = 2
 step    index   ch    res
 Init    0       P     ["", "", ""]
 0       0       P     ["P", "", ""]
 1       1       A     ["P", "A", ""]
-1       2       Y     ["P", "A", "Y"]
-1       1       P     ["P", "AP", "Y"]
 1       0       A     ["PA", "AP", "Y"]
 1       1       L     ["PA", "APL", "Y"]
-1       2       I     ["PA", "APL", "YI"]
-1       1       S     ["PA", "APLS", "YI"]
 1       0       H     ["PAH", "APLS", "YI"]
 1       1       I     ["PAH", "APLSI", "YI"]
-1       2       R     ["PAH", "APLSI", "YIR"]
-1       1       I     ["PAH", "APLSII", "YIR"]
 1       0       N     ["PAHN", "APLSII", "YIR"]
 1       1       G     ["PAHN", "APLSIIG", "YIR"]

 - join the res -> "PAHNAPLSIIGYIR"

Intuition

Maintain a step that changes with following condition
1. If the index is equal to len(string) -1
    - reset step to -1 because we want to move back up the matrix diagonally
2. else if index is at 0 that would mean that we have reached the top row and therefore we can set step starting at 1


Algorithm

1. Base Case
    a. check if number of rows is one
    b. check if the number of rows is greater than the length of the string
    both will result in the whole string printed as is
2. Initialize Variables
    a. res -> store result in a list [here matrix is represented by string of list]
    b. index -> going through the string [also in reference to the rows in the matrix]
    c. step -> used to add the items diagonally in between like zig zag for calculation
3. Loop the string and for each charachter
    a. Add at the index
    b. check if index is 0 [this would mean that we are filling that column completely]
        - therefore set step to be incremented by 1
    c. check if index is equal to number of rows - 1
        - therefore steo should be set to -1 as we need to go back up the rows diagonally filling
    d. Finally increment the index per step
5. After loop join the result array and return.

"""

class Solution:
    def convert(self, s, numRows):
        if numRows == 1 or numRows >= len(s):
          return s
        # Initialize result, index, step
        res, index, step = [''] * numRows, 0, 0
        # For each charachter

        for ch in s:
          res[index] += ch
          if index == 0:
            step = 1
          elif index == numRows - 1:
            step = -1
          index += step
        return "".join(res)


assert Solution().convert("PAYPALISHIRING", 3) == "PAHNAPLSIIGYIR"
assert Solution().convert("PAYPALISHIRING", 4) == "PINALSIGYAHRPI"