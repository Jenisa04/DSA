class Solution:
    # Jenisa
    def sumZero(self, n: int) -> List[int]:
        ans = []
        if n==1:
            ans.append(0)
        else:
            i = 1
            while(i<n):
                ans.append(i)
                ans.append(i*-1)
                i+=2
            if(n%2!=0):
                ans.append(0)
        return ans