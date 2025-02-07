class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        
        sMap = {}

        for j in stones:
            if j in sMap:
                sMap[j] += 1
            else:
                sMap[j] = 1
        
        count = 0
        for k in jewels:
            if k in sMap:
                count += sMap[k]

        return count