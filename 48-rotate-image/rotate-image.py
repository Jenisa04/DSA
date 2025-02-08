class Solution:
    # Jenisa
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # Approach 2: Transpose first and then reverse
        for r in range(len(matrix)):
            for c in range(r+1, len(matrix)):
                matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]
        for row in matrix:
            row.reverse()