class Solution:
    # Jenisa
    def reversePrefix(self, word: str, ch: str) -> str:
        if ch not in word:
            return word
        
        reverseStr = []
        idx = 0
        for index, i in enumerate(word):
            if i == ch:
                reverseStr.append(i)
                idx = index
                break
            reverseStr.append(i)
        reverseStr.reverse()
        reverseStr = ''.join(reverseStr)
        reverseStr += word[idx+1:]
        return reverseStr