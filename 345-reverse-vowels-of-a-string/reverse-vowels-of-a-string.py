class Solution:
    # Jenisa
    def reverseVowels(self, s: str) -> str:
        word = list(s)
        vowelsList = ['a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U']
        start = 0
        end = len(s) - 1
        while start <= end:
            if word[start] in vowelsList:
                if word[end] in vowelsList:
                    temp = word[start]
                    word[start] = word[end]
                    word[end] = temp
                    start += 1
                    end -= 1
                else:
                    end -= 1
                
            else:
                start += 1

        word = ''.join(word)
        return word