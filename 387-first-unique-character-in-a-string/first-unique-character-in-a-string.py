class Solution:
    def firstUniqChar(self, s: str) -> int:
        char = dict()
        for i in s:
            if i not in char:
                char[i] = 1
            else:
                char[i] += 1
        
        tempChar = ''
        for key,val in char.items():
            if val == 1:
                tempChar+=key
                break

        if len(tempChar) > 0:
            for j in range(len(s)):
                if tempChar[0] == s[j]:
                    return j
        return -1
