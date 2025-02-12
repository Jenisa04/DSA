class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        newMat = []
        numRows = len(matrix)
        numCols = len(matrix[0])

        for c in range(numCols):
            temp = []
            for r in range(numRows):
                temp.append(matrix[r][c])
            newMat.append(temp)
        
        return newMat