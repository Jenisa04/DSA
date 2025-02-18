# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        l = 0
        r = n
        while l<=r:
            m = l + (r-l)//2
            badVersion = isBadVersion(m)
            if badVersion==True:
                r=m-1
            else:
                l=m+1
        return l