class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        allNums = set(range(1,n**2 + 1))
        gridNums = set()
        repeatNum = 0
        for i in range(n):
            for j in range(n):
                if grid[i][j] not in gridNums:
                    gridNums.add(grid[i][j])
                else:
                    repeatNum = grid[i][j]

        missingNum = allNums - gridNums
        return [repeatNum, list(missingNum)[0]]
            