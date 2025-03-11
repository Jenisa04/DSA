class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        l = 0
        n = len(s)
        total = 0
        lettersFreq = [0] * 3
        for r in range(n):
            lettersFreq[ord(s[r]) - ord('a')] += 1

            while self.hasReqLetters(lettersFreq):
                total+= len(s) - r

                lettersFreq[ord(s[l]) - ord('a')] -= 1
                l+=1
        return total

    def hasReqLetters(self, freq: list) -> bool:
        return all(f>0 for f in freq)
            