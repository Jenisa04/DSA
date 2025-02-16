class Solution:
    # Jenisa
    def mySqrt(self, x: int) -> int:
        l = 0
        r = x//2 +1
        while l<=r:
            m = l + (r-l) // 2
            sq = m*m
            if sq == x:
                return m
            elif sq < x:
                l = m+1
            else:
                r = m-1
            
        return r