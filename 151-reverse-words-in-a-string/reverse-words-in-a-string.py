class Solution:
    # Jenisa
    def reverseWords(self, s: str) -> str:
        words = s.split()
        start = 0
        end = len(words) - 1
        while start <= end:
            temp = words[start]
            words[start] = words[end]
            words[end] = temp
            start += 1
            end -= 1

        temp = ' '. join(words)
        return temp