class Solution:
    # Jenisa
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1:
            return [[1]]

        trngl = [[1]]
        for i in range(1,numRows):
            prevRow = trngl[-1]
            currRow = [1]
            for j in range(1, len(prevRow)):
                currRow.append(prevRow[j-1] + prevRow[j])
            currRow.append(1)

            trngl.append(currRow)

        return trngl