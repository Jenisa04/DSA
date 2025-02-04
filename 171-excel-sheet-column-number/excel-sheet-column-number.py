class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        # traverse through the column title from the end
        # so A = 26
        # AB = (26^len(title)-index-1 * 1) + (2)
        # ABC = (26^2 * 1) + (26^1 * 2) + (3)
        n = len(columnTitle)
        res = 0
        for i in range(n):
            res += (26**(n-i-1) * (ord(columnTitle[i]) - ord('A') + 1))

        return res