class Solution:
    # Jenisa
    def mergeAlternately(self, word1: str, word2: str) -> str:
        temp = ""
        if len(word1) >= len(word2):
            for i in range(len(word2)):
                temp += word1[i] + word2[i]
            temp += word1[len(word2):]
        
        if len(word1) < len(word2):
            for i in range(len(word1)):
                temp += word1[i] + word2[i]
            temp += word2[len(word1):]
        
        return temp