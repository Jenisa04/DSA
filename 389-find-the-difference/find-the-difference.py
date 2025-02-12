from collections import Counter

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        if len(s) == 0:
            return t
        
        count = dict()

        for char in t:
            count[char] = count.get(char, 0) + 1

        for char in s:
            count[char] -= 1
            if count[char] == 0:
                del count[char]
        res = list(count.keys())[0]
        return res
