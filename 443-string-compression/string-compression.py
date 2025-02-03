class Solution:
    def compress(self, chars: List[str]) -> int:
        
        if len(chars) == 1:
            return 1
        
        i = 0
        while i <= len(chars)-1:
            currLetter = chars[i]
            currCount = 1

            for j in range(i+1, len(chars)):
                if chars[j] == currLetter:
                    currCount +=1
                else:
                    break
            
            if currCount == 1:
                i += 1
    
            else:
                chars[i+1 : i+currCount] = list(str(currCount))
                i+=len(str(currCount)) + 1

        return len(chars)