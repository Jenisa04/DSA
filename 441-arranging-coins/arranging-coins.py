class Solution:
    def arrangeCoins(self, n: int) -> int:
        total = n
        i = 1
        rowCount = 0
        while total>=0:
            total -= i
            i+=1
            rowCount+=1
        
        return rowCount-1