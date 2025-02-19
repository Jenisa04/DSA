class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) == len(t) == 1: 
            if s==t: return True
            else: return False

        rec = dict()

        for i in range(len(s)):
            if s[i] in rec:
                if rec[s[i]] != t[i]:
                    return False

            elif t[i] in rec.values():
                return False
                
            rec[s[i]] = t[i]
        
        return True
        
            
