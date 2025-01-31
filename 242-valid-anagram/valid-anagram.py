class Solution:
    # Jenisa
    def isAnagram(self, s: str, t: str) -> bool:
        hm1 = {}
        hm2 = {}

        if len(s) != len(t):
            return False

        for i in range(len(s)):
            if s[i] in hm1:
                hm1[s[i]] += 1
            else:
                hm1[s[i]] = 1

            if t[i] in hm2:
                hm2[t[i]] += 1
            else:
                hm2[t[i]] = 1


        if (hm1==hm2):
            return True
        else:
            return False