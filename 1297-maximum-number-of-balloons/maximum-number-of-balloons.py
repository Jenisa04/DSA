class Solution(object):
    # Jenisa
    def maxNumberOfBalloons(self, text):
        """
        :type text: str
        :rtype: int
        """
        reqCharCt = {'b':0, 'a':0, 'l':0, 'o':0, 'n':0}

        for i in text:
            if i in reqCharCt:
                reqCharCt[i] += 1
        
        # if reqCharCt['l']>=2 and reqCharCt['o']>= 2:
        return min(reqCharCt['b'], reqCharCt['a'], reqCharCt['n'], reqCharCt['l']//2, reqCharCt['o']//2) 

        # return 0 