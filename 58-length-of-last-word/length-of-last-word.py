class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        temp = s.split()
        lastWord = temp[-1]
        return len(lastWord)