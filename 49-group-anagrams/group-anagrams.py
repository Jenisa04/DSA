from collections import Counter
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) == 1:
            return [strs]
        allAnagrams = {}

        for term in strs:
            sortedVal = "".join(sorted(term))
            if sortedVal in allAnagrams:
                allAnagrams[sortedVal].append(term)
            else:
                allAnagrams[sortedVal] = [term]
        
        return(list(allAnagrams.values()))