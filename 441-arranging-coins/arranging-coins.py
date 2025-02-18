class Solution:
    def arrangeCoins(self, n: int) -> int:
        # sum of int 1 to n formula:
        # k(k+1)//2 = n
        # restructuring this to get
        # (-1+(1+8n)**(1/2)) // 2
        return int((-1 + (1+8*n)**(1/2)) // 2)
        