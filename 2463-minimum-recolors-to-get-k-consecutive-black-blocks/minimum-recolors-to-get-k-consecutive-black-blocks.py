from collections import Counter

class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        n = len(blocks)
        count = 0
        if n==k:
            for i in range(n):
                if blocks[i] == 'W':
                    count +=1
        else:
            minCtr = 101
            for i in range(n-k+1):
                blocksCtr = Counter(blocks[i:i+k])
                if blocksCtr['W'] == 0:
                    return 0
                minCtr = min(minCtr, blocksCtr['W'])
                
            count = minCtr  
        
        return count