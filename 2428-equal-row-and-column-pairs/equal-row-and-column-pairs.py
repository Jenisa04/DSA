class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        # columns = []
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
            # columns.append(column)
            column = []
        # print(ct)
        # now iterate through all the lists in grid and check if it matches with a list in columns
        # count = 0
        # for i in range(len(grid)):
        #     for j in range(len(columns)):
        #         if grid[i] == columns[j]:
        #             count += 1
        return ct