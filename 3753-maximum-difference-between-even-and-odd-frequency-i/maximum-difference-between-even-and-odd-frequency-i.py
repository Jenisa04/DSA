class Solution:
    def maxDifference(self, s: str) -> int:
        oddFreq = 0
        evenFreq = 100
        freq = dict()
        for i in range(len(s)):
            if s[i] not in freq:
                freq[s[i]] = 1
            else:
                freq[s[i]] += 1
        
        for key, val in freq.items():
            if val%2==0:
                evenFreq = min(evenFreq, val)
            else:
                oddFreq = max(oddFreq, val)
        return oddFreq - evenFreq