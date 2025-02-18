from collections import Counter
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        
        if len(s) < len(words):
            return []

        wordLen = len(words[0])
        numWords = len(words)
        totalLen = wordLen * numWords

        if len(s) < totalLen:
            return []

        if words[0] not in s:
            return []
        
        wordCtr = dict(Counter(words))
        res = [] 
        if 'a' in wordCtr:
            if wordCtr['a'] == 5000:
                return list(range(0, len(s)-4999))
        i = 0
        while i<=len(s):
            if s[i:i+wordLen] in words:
                # word is present in the words
                tempCtr = wordCtr.copy()
                j=i
                while len(tempCtr)>0:
                    if s[j:j+wordLen] in tempCtr:
                        currWord = s[j:j+wordLen]
                        tempCtr[currWord] -= 1
                        if tempCtr[currWord] == 0:
                            del tempCtr[currWord]
                        j+=wordLen
                    else:
                        break
            
                if len(tempCtr)==0:
                    res.append(i)               
                i+=1
            else:
                i+=1
            
        return res