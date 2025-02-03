class Solution(object):
    def maxValue(self, n, x):
        """
        :type n: str
        :type x: int
        :rtype: str
        """

        if (n[0] == '-'):
            pos = 1
            while(pos < len(n) and int(n[pos]) <= x):
                pos+=1
        else:
            pos = 0
            while (pos < len(n) and int(n[pos]) >= x):
                pos+=1
                
        return n[:pos] + str(x) + n[pos:]