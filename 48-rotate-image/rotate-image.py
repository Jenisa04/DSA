import copy
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        nums = copy.deepcopy(matrix)
        numCols = numRows = len(nums)
        for r in range(numRows):
            for c in range(numCols):
                matrix[c][numRows-r-1] = nums[r][c]