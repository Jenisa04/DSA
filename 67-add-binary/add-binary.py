class Solution:
    # Jenisa
    def addBinary(self, a: str, b: str) -> str:
        res = ""
        i = len(a)-1
        j = len(b)-1
        carry = 0

        while i>=0 or j>=0 or carry:
            if i>=0:
                carry+=int(a[i])
                i-=1
            if j>=0:
                carry+=int(b[j])
                j-=1
            res = str(carry%2)+res
            carry//=2
        
        return res