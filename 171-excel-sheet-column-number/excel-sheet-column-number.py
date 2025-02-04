class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        # traverse through the column title
        # get values of alphabets from ASCII 
        # making 'A' (65)- 1 and subtracting the rest to get positions
        # so 'B' = 66 - 65 + 1 (+1 for 1-indexed)
        # AB = (26^len(title)-index-1 * 1) + (2)
        # ABC = (26^2 * 1) + (26^1 * 2) + (3)
        n = len(columnTitle)
        res = 0
        for i in range(n):
            res += (26**(n-i-1) * (ord(columnTitle[i]) - ord('A') + 1))

        return res