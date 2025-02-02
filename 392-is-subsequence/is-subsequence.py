class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        if len(s) > len(t): return False
        if len(s) < 1: return True
    
        j = 0
        for i in range(len(t)):
            if j <= len(s)-1 and t[i] == s[j]:
                    j+=1
  
      
        return j == len(s)
                   