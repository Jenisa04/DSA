from collections import Counter

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        rnCount = dict(Counter(ransomNote))
        mCount = dict(Counter(magazine))

        for key, val in rnCount.items():
            if key not in mCount:
                return False
            if mCount[key] < val:
                return False

        return True