class Solution:
    # Jenisa
    def longestPalindrome(self, s: str) -> int:
        chars = set()
        length = 0

        for char in s:
            if char in chars:
                chars.remove(char)
                length += 2
            else:
                chars.add(char)

        if chars:
            length+=1

        return length
