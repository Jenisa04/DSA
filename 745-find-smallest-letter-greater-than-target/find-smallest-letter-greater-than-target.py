class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        if target>=letters[-1] or target < letters[0]:
            return letters[0]
        l = 0
        r= len(letters) - 1
        
        while l<=r:
            m = l + (r-l) // 2
            if target >= letters[m]:
                l = m+1
            if target < letters[m]:
                r = m-1
        
        return letters[l]