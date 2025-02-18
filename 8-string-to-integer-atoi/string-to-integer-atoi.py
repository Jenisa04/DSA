class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.lstrip()
        if len(s)==0:
            return 0

        sign = 1
        if s[0] == '-':
            sign = -1
            s = s[1:]
        elif s[0] == '+':
            s=s[1:]
            
        res = 0
        for idx,val in enumerate(s):
            if val.isdigit():
                res = res*10 + int(val)
            else:
                break
        
        temp = res * sign
        if temp < ((-2)**31):
            return int((-2)**31)
        elif temp > (2**31 - 1):
            return int(2**31 - 1)
        return temp
