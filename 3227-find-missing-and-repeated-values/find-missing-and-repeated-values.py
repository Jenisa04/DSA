class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        allNums = set(range(1,n**2 + 1))
        repeatNum = 0
        for i in range(n):
            for j in range(n):
                if grid[i][j] in allNums:
                    allNums.remove(grid[i][j])
                else:
                    repeatNum = grid[i][j]

        return [repeatNum, list(allNums)[0]]