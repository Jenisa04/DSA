class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        if len(strs) <= 1:
            return [strs]
        anagrams = {}
        
        for s in strs:
            # Use the sorted string as a key
            key = ''.join(sorted(s))
            
            # If the key is not already in the dictionary, add it
            if key not in anagrams:
                anagrams[key] = []
            
            # Append the current string to the list corresponding to the key
            anagrams[key].append(s)
        
        # Return the grouped anagrams as a list
        return list(anagrams.values())
