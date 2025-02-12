class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        n = num//2
        found = False

        l = 0
        r = num

        while l<= r:
            m = (l+r)//2
            sq = m**2
            if sq == num:
                return True
            elif sq < num:
                l = m + 1
            else:
                r = m-1
        return False