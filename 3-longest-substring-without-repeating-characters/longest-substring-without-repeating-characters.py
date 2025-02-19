class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0: return 0
        if len(s) == 1 or len(set(s))==1: return 1
        if len(s) == len(set(s)): return len(s)
        maxLen = 0
        temp = ''
        
        for i in range(len(s)):
            temp = s[i]
            if i == len(s)-1:
                maxLen = max(maxLen, len(temp))
                break
            r = i+1
            if s[r] not in temp:
                while r<len(s):
                    if s[r] not in temp:
                        temp+=s[r]
                        maxLen = max(maxLen, len(temp))
                        r+=1
                    else:
                        break
            
        return maxLen