class Solution:
    def reverse(self, x: int) -> int:
        num = str(x)
     
        if num[0] == '-':
            temp = int('-' + num[-1:0:-1])
        else:
            temp = int(num[-1:0:-1] + num[0])        
        
        if temp<2147483647 and temp>-2147483648:
            return temp
            
        return 0
        
        