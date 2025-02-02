class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        column = []
        ct = 0
        for col in range(len(grid)):
            row = 0
            while row != len(grid[col]):
                column.append(grid[row][col])
                row+=1
            for allRows in grid:
                if allRows == column:
                    ct+=1
            column = []
        return ct