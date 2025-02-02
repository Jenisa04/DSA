class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        columns = []
        column = []
        for col in range(len(grid)):
            row = 0
            while row != len(grid[col]):
                column.append(grid[row][col])
                row+=1
            columns.append(column)
            column = []

        # now iterate through all the lists in grid and check if it matches with a list in columns
        count = 0
        for i in range(len(grid)):
            for j in range(len(columns)):
                if grid[i] == columns[j]:
                    count += 1
        return count