import math
class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        if n==1:
            return True
        
        def logarithm(n) -> int:
            return round(math.log(n) / math.log(3), 10)
        
        res = []
        num = n
        while num>0:
            logNum = int(logarithm(num))
            if logNum not in res:
                res.append(logNum)
            else:
                return False

            sub = pow(3, res[-1])
            num -= sub
        
        return True